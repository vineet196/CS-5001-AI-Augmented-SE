"""GitHub API helpers using PyGithub."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from github import Github, GithubException

import config


def _client() -> Github:
    if not config.GITHUB_TOKEN:
        raise RuntimeError("GITHUB_TOKEN is not set. Add it to your .env file.")
    return Github(config.GITHUB_TOKEN)


# ---------------------------------------------------------------------------
# Data classes for structured data exchange between agents
# ---------------------------------------------------------------------------

@dataclass
class IssueData:
    title: str
    body: str
    labels: list[str] | None = None


@dataclass
class PRData:
    title: str
    body: str
    head: str          # source branch
    base: str = "main" # target branch
    labels: list[str] | None = None


@dataclass
class ExistingItem:
    """Represents a fetched issue or PR."""
    number: int
    title: str
    body: str
    state: str
    labels: list[str]
    item_type: str  # "issue" or "pull_request"
    comments: list[str] | None = None


# ---------------------------------------------------------------------------
# Issue operations
# ---------------------------------------------------------------------------

def create_issue(repo_name: str, data: IssueData) -> str:
    """Create a GitHub issue. Returns the issue URL."""
    gh = _client()
    repo = gh.get_repo(repo_name)
    issue = repo.create_issue(
        title=data.title,
        body=data.body,
        labels=data.labels or [],
    )
    return issue.html_url


def fetch_issue(repo_name: str, number: int) -> ExistingItem:
    """Fetch an existing issue by number."""
    gh = _client()
    repo = gh.get_repo(repo_name)
    issue = repo.get_issue(number)
    comments = [c.body for c in issue.get_comments()]
    return ExistingItem(
        number=issue.number,
        title=issue.title,
        body=issue.body or "",
        state=issue.state,
        labels=[l.name for l in issue.labels],
        item_type="issue",
        comments=comments,
    )


def update_issue(repo_name: str, number: int, data: IssueData) -> str:
    """Update an existing issue's title and body. Returns the issue URL."""
    gh = _client()
    repo = gh.get_repo(repo_name)
    issue = repo.get_issue(number)
    issue.edit(title=data.title, body=data.body)
    return issue.html_url


# ---------------------------------------------------------------------------
# Pull-request operations
# ---------------------------------------------------------------------------

def create_pull_request(repo_name: str, data: PRData) -> str:
    """Create a GitHub pull request. Returns the PR URL."""
    gh = _client()
    repo = gh.get_repo(repo_name)
    pr = repo.create_pull(
        title=data.title,
        body=data.body,
        head=data.head,
        base=data.base,
    )
    if data.labels:
        pr.set_labels(*data.labels)
    return pr.html_url


def fetch_pull_request(repo_name: str, number: int) -> ExistingItem:
    """Fetch an existing pull request by number."""
    gh = _client()
    repo = gh.get_repo(repo_name)
    pr = repo.get_pull(number)
    comments = [c.body for c in pr.get_issue_comments()]
    return ExistingItem(
        number=pr.number,
        title=pr.title,
        body=pr.body or "",
        state=pr.state,
        labels=[l.name for l in pr.labels],
        item_type="pull_request",
        comments=comments,
    )


def update_pull_request(repo_name: str, number: int, data: PRData) -> str:
    """Update an existing PR title and body. Returns the PR URL."""
    gh = _client()
    repo = gh.get_repo(repo_name)
    pr = repo.get_pull(number)
    pr.edit(title=data.title, body=data.body)
    return pr.html_url
