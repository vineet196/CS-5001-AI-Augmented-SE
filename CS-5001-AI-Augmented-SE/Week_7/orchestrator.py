"""Orchestrator — coordinates multi-agent flows for all three tasks."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Confirm

import config
from agents import reviewer, planner, writer, gatekeeper
from tools import git_tools, github_api

console = Console()


@dataclass
class FlowResult:
    """Outcome of an orchestrated flow."""
    action_taken: str          # "created_issue", "created_pr", "improved", "none"
    url: str | None = None     # GitHub URL if something was created/updated
    draft: writer.Draft | None = None
    review: reviewer.DiffReview | None = None


# ---------------------------------------------------------------------------
# Task 1: agent review
# ---------------------------------------------------------------------------

def review_flow(
    repo: str,
    base_branch: str = "main",
    commit_range: str | None = None,
    cwd: str | None = None,
) -> FlowResult:
    """Full review pipeline: Reviewer → Planner → Writer → Gatekeeper."""

    # Step 1 — get the diff
    console.print("[bold cyan][Reviewer][/] Fetching diff…")
    if commit_range:
        diff = git_tools.get_range_diff(commit_range, cwd=cwd)
    else:
        diff = git_tools.get_diff(base_branch, cwd=cwd)

    if not diff.strip():
        console.print("[yellow]No changes found.[/]")
        return FlowResult(action_taken="none")

    # Step 2 — Reviewer
    console.print("[bold cyan][Reviewer][/] Analyzing diff…")
    rev = reviewer.review_diff(diff)
    _print_review(rev)

    # Step 3 — Planner
    console.print("[bold yellow][Planner][/] Deciding on action…")
    plan = planner.plan_from_review(rev)
    _print_plan(plan)

    if plan.action == "none":
        console.print("[green]No action needed.[/]")
        return FlowResult(action_taken="none", review=rev)

    # Step 4 — Writer + Gatekeeper loop
    console.print("[bold green][Writer][/] Drafting…")
    draft = writer.draft_from_plan(plan)
    draft = _gatekeeper_loop(draft)
    _print_draft(draft)

    # Step 5 — Approval
    _approval_gate(repo, draft, base_branch, cwd)

    return FlowResult(
        action_taken="created_issue" if draft.item_type == "issue" else "created_pr",
        draft=draft,
        review=rev,
    )


# ---------------------------------------------------------------------------
# Task 2: agent draft issue / agent draft pr
# ---------------------------------------------------------------------------

def draft_flow(
    repo: str,
    instruction: str,
    item_type: str = "issue",
    base_branch: str = "main",
    cwd: str | None = None,
) -> FlowResult:
    """Draft an issue/PR from a user instruction."""

    # Gather optional context
    context_parts: list[str] = []
    try:
        diff = git_tools.get_diff(base_branch, cwd=cwd)
        if diff.strip():
            context_parts.append(f"## Git diff\n```\n{diff[:8000]}\n```")
    except RuntimeError:
        pass
    context = "\n\n".join(context_parts)

    # Planner — scope validation
    console.print("[bold yellow][Planner][/] Scope validated.")
    plan = planner.plan_from_instruction(instruction, context)
    # Force the item_type chosen by the user
    plan.item_type = item_type
    plan.action = "create_issue" if item_type == "issue" else "create_pr"
    _print_plan(plan)

    # Writer + Gatekeeper
    console.print("[bold green][Writer][/] Draft created.")
    draft = writer.draft_from_plan(plan)
    draft = _gatekeeper_loop(draft)
    _print_draft(draft)

    # Approval
    _approval_gate(repo, draft, base_branch, cwd)

    return FlowResult(
        action_taken="created_issue" if draft.item_type == "issue" else "created_pr",
        draft=draft,
    )


# ---------------------------------------------------------------------------
# Task 3: agent improve issue / agent improve pr
# ---------------------------------------------------------------------------

def improve_flow(
    repo: str,
    number: int,
    item_type: str = "issue",
) -> FlowResult:
    """Improve an existing issue or PR."""

    label = _capitalize_type(item_type)

    # Fetch
    console.print(f"[bold cyan][Reviewer][/] Fetching {label} #{number}…")
    if item_type == "issue":
        item = github_api.fetch_issue(repo, number)
    else:
        item = github_api.fetch_pull_request(repo, number)

    # Reviewer critique
    console.print(f"[bold cyan][Reviewer][/] Critiquing {label}…")
    critique = reviewer.critique_item(item.title, item.body)
    _print_critique(critique)

    # Writer improvement
    console.print("[bold green][Writer][/] Proposed improved structured version.")
    improved = writer.improve_existing(item.title, item.body, critique)
    improved.item_type = item.item_type

    # Gatekeeper comparison
    console.print("[bold magenta][Gatekeeper][/] Comparing versions…")
    comparison = gatekeeper.reflect_improvement(item.title, item.body, improved)
    _print_improvement_comparison(comparison)
    _print_draft(improved)

    verdict = "PASS" if comparison.verdict == "BETTER" else "FAIL"
    console.print(f"[bold magenta][Gatekeeper][/] Reflection verdict: {verdict}")

    if comparison.verdict == "NOT_BETTER":
        console.print("[yellow]Gatekeeper says improvement is not clearly better. Showing anyway.[/]")

    # User approval
    approved = Confirm.ask("\n[bold]Approve update? (yes to push, no to abort)[/]")
    if approved:
        console.print(f"[bold magenta][Gatekeeper][/] Updating {label} on GitHub…")
        if item_type == "issue":
            url = github_api.update_issue(
                repo, number,
                github_api.IssueData(title=improved.title, body=improved.body, labels=improved.labels),
            )
        else:
            url = github_api.update_pull_request(
                repo, number,
                github_api.PRData(
                    title=improved.title, body=improved.body,
                    head="", base="",
                    labels=improved.labels,
                ),
            )
        console.print(f"[bold green][Tool][/] GitHub API call successful. Updated: {url}")
        return FlowResult(action_taken="improved", url=url, draft=improved)
    else:
        console.print("[bold red][Gatekeeper][/] Draft rejected. No changes made.")
        return FlowResult(action_taken="none", draft=improved)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _gatekeeper_loop(draft: writer.Draft) -> writer.Draft:
    """Run the gatekeeper reflection loop, revising up to MAX_REVISION_CYCLES."""
    for cycle in range(config.MAX_REVISION_CYCLES):
        console.print(f"[bold magenta][Gatekeeper][/] Reflection pass {cycle + 1}…")
        reflection = gatekeeper.reflect(draft)
        if reflection.verdict == "PASS":
            console.print(f"[bold magenta][Gatekeeper][/] Reflection verdict: PASS (score {reflection.score}/10)")
            return draft
        console.print(
            f"[bold magenta][Gatekeeper][/] Reflection verdict: FAIL — {reflection.feedback[:80]}"
        )
        console.print("[bold green][Writer][/] Revision required. Revising…")
        draft = writer.revise_draft(draft, reflection.feedback)
    console.print("[yellow][Gatekeeper] Max revision cycles reached, using latest draft.[/]")
    return draft


def _approval_gate(
    repo: str,
    draft: writer.Draft,
    base_branch: str,
    cwd: str | None,
) -> None:
    """Show approve/reject prompt; submit to GitHub or abort."""
    approved = Confirm.ask("\n[bold]Approve? (yes to create, no to abort)[/]")
    if approved:
        label = _capitalize_type(draft.item_type)
        console.print(f"[bold magenta][Gatekeeper][/] Creating {label}…")
        url = _submit(repo, draft, base_branch, cwd)
        console.print(f"[bold green][Tool][/] GitHub API call successful. Created: {url}")
    else:
        console.print("[bold red][Gatekeeper][/] Draft rejected. No changes made.")


def _submit(
    repo: str,
    draft: writer.Draft,
    base_branch: str,
    cwd: str | None,
) -> str:
    """Submit a draft to GitHub and return the URL."""
    if draft.item_type == "issue":
        return github_api.create_issue(
            repo,
            github_api.IssueData(title=draft.title, body=draft.body, labels=draft.labels),
        )
    else:
        head = git_tools.get_current_branch(cwd=cwd)
        if head == base_branch:
            console.print(
                f"[bold red][Error][/] You're on '{head}' — cannot create a PR "
                f"from '{head}' to '{base_branch}'.\n"
                f"Create a feature branch first:\n"
                f"  git checkout -b feature/your-change\n"
                f"  git add . && git commit -m 'your message'\n"
                f"  git push -u origin feature/your-change\n"
                f"  agent review --base {base_branch}"
            )
            raise SystemExit(1)
        return github_api.create_pull_request(
            repo,
            github_api.PRData(
                title=draft.title,
                body=draft.body,
                head=head,
                base=base_branch,
                labels=draft.labels,
            ),
        )


def _capitalize_type(item_type: str) -> str:
    return "Pull Request" if item_type == "pull_request" else "Issue"


def _print_review(rev: reviewer.DiffReview) -> None:
    body = (
        f"**Summary:** {rev.summary}\n\n"
        f"**Type:** {rev.change_type} | **Risk:** {rev.risk_level}\n\n"
    )
    if rev.issues:
        body += "**Issues:**\n"
        for i in rev.issues:
            body += f"- [{i.get('severity', '?')}] {i.get('file', '?')}: {i.get('description', '')}\n"
    if rev.positive_notes:
        body += "\n**Positive:**\n"
        for n in rev.positive_notes:
            body += f"- {n}\n"
    console.print(Panel(Markdown(body), title="[cyan]Reviewer Analysis[/]", border_style="cyan"))


def _print_plan(plan: planner.Plan) -> None:
    body = (
        f"**Action:** {plan.action}\n\n"
        f"**Title:** {plan.suggested_title}\n\n"
        f"**Justification:** {plan.justification}\n\n"
        f"**Evidence:**\n"
    )
    for e in plan.evidence:
        body += f"- {e}\n"
    console.print(Panel(Markdown(body), title="[yellow]Planner Decision[/]", border_style="yellow"))


def _print_draft(draft: writer.Draft) -> None:
    body = f"# {draft.title}\n\n{draft.body}\n\n---\nLabels: {', '.join(draft.labels)}"
    console.print(Panel(Markdown(body), title=f"[green]Draft ({_capitalize_type(draft.item_type)})[/]", border_style="green"))


def _print_critique(critique: reviewer.Critique) -> None:
    body = (
        f"**Clarity:** {critique.clarity_score}/10 | **Completeness:** {critique.completeness_score}/10\n\n"
    )
    if critique.problems:
        body += "**Problems:**\n"
        for p in critique.problems:
            body += f"- {p}\n"
    if critique.suggestions:
        body += "\n**Suggestions:**\n"
        for s in critique.suggestions:
            body += f"- {s}\n"
    console.print(Panel(Markdown(body), title="[red]Critique[/]", border_style="red"))


def _print_improvement_comparison(comp: gatekeeper.ImprovementReflection) -> None:
    body = (
        f"**Verdict:** {comp.verdict}\n\n"
        f"**Score:** {comp.score_before}/10 → {comp.score_after}/10\n\n"
    )
    if comp.improvements:
        body += "**Improvements:**\n"
        for i in comp.improvements:
            body += f"- {i}\n"
    if comp.regressions:
        body += "\n**Regressions:**\n"
        for r in comp.regressions:
            body += f"- {r}\n"
    body += f"\n{comp.feedback}"
    console.print(Panel(Markdown(body), title="[magenta]Gatekeeper Comparison[/]", border_style="magenta"))
