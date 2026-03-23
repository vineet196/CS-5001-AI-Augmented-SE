#!/usr/bin/env python3
"""CLI entry point for the GitHub Agent.

Usage examples:
    agent review --base main
    agent review --range HEAD~3..HEAD
    agent draft issue --instruction "Add rate limiting to login endpoint"
    agent draft pr   --instruction "Refactor duplicated pricing logic"
    agent improve issue --number 42
    agent improve pr   --number 17
"""

from typing import Optional

import typer
from rich.console import Console

console = Console()

# ── Top-level app ──────────────────────────────────────────────────────────
app = typer.Typer(
    name="agent",
    help="Multi-agent GitHub assistant: review diffs, draft issues/PRs, improve existing items.",
    add_completion=False,
)

# ── Subcommand groups ──────────────────────────────────────────────────────
draft_app = typer.Typer(help="Draft a new GitHub issue or PR from a natural-language instruction.")
improve_app = typer.Typer(help="Improve an existing GitHub issue or PR.")

app.add_typer(draft_app, name="draft")
app.add_typer(improve_app, name="improve")


# ---------------------------------------------------------------------------
# agent review
# ---------------------------------------------------------------------------
@app.command()
def review(
    base: str = typer.Option("main", "--base", "-b", help="Base branch to diff against"),
    range: Optional[str] = typer.Option(None, "--range", "-r", help="Commit range (e.g. HEAD~3..HEAD)"),
    repo: Optional[str] = typer.Option(None, "--repo", help="GitHub repo owner/name (reads from git remote if omitted)"),
    cwd: Optional[str] = typer.Option(None, "--cwd", "-C", help="Git working directory"),
):
    """Review the current branch diff and optionally create an issue or PR."""
    from orchestrator import review_flow

    resolved_repo = repo or _detect_repo(cwd)
    review_flow(repo=resolved_repo, base_branch=base, commit_range=range, cwd=cwd)


# ---------------------------------------------------------------------------
# agent draft issue / agent draft pr
# ---------------------------------------------------------------------------
@draft_app.command("issue")
def draft_issue(
    instruction: str = typer.Option(..., "--instruction", "-i", help="What the issue should describe"),
    repo: Optional[str] = typer.Option(None, "--repo", help="GitHub repo owner/name"),
    base: str = typer.Option("main", "--base", "-b", help="Base branch for context"),
    cwd: Optional[str] = typer.Option(None, "--cwd", "-C", help="Git working directory"),
):
    """Draft a new GitHub issue from a natural-language instruction."""
    from orchestrator import draft_flow

    resolved_repo = repo or _detect_repo(cwd)
    draft_flow(repo=resolved_repo, instruction=instruction, item_type="issue", base_branch=base, cwd=cwd)


@draft_app.command("pr")
def draft_pr(
    instruction: str = typer.Option(..., "--instruction", "-i", help="What the PR should describe"),
    repo: Optional[str] = typer.Option(None, "--repo", help="GitHub repo owner/name"),
    base: str = typer.Option("main", "--base", "-b", help="Base branch for PR target"),
    cwd: Optional[str] = typer.Option(None, "--cwd", "-C", help="Git working directory"),
):
    """Draft a new GitHub pull request from a natural-language instruction."""
    from orchestrator import draft_flow

    resolved_repo = repo or _detect_repo(cwd)
    draft_flow(repo=resolved_repo, instruction=instruction, item_type="pull_request", base_branch=base, cwd=cwd)


# ---------------------------------------------------------------------------
# agent improve issue / agent improve pr
# ---------------------------------------------------------------------------
@improve_app.command("issue")
def improve_issue(
    number: int = typer.Option(..., "--number", "-n", help="Issue number to improve"),
    repo: Optional[str] = typer.Option(None, "--repo", help="GitHub repo owner/name"),
    cwd: Optional[str] = typer.Option(None, "--cwd", "-C", help="Git working directory"),
):
    """Improve an existing GitHub issue."""
    from orchestrator import improve_flow

    resolved_repo = repo or _detect_repo(cwd)
    improve_flow(repo=resolved_repo, number=number, item_type="issue")


@improve_app.command("pr")
def improve_pr(
    number: int = typer.Option(..., "--number", "-n", help="PR number to improve"),
    repo: Optional[str] = typer.Option(None, "--repo", help="GitHub repo owner/name"),
    cwd: Optional[str] = typer.Option(None, "--cwd", "-C", help="Git working directory"),
):
    """Improve an existing GitHub pull request."""
    from orchestrator import improve_flow

    resolved_repo = repo or _detect_repo(cwd)
    improve_flow(repo=resolved_repo, number=number, item_type="pull_request")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _detect_repo(cwd: Optional[str] = None) -> str:
    """Try to detect owner/repo from the git remote URL."""
    import re
    from tools.git_tools import _run

    try:
        url = _run(["git", "remote", "get-url", "origin"], cwd=cwd)
        # SSH:  git@github.com:owner/repo.git
        # HTTPS: https://github.com/owner/repo.git
        m = re.search(r"[:/]([^/]+/[^/]+?)(?:\.git)?$", url)
        if m:
            return m.group(1)
    except RuntimeError:
        pass
    console.print("[red]Could not detect repo from git remote. Use --repo owner/name.[/]")
    raise typer.Exit(1)


if __name__ == "__main__":
    app()
