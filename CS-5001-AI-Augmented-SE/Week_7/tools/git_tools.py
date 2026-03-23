"""Git tools — thin wrappers around subprocess for git operations."""

import subprocess
from pathlib import Path
from typing import Optional


def _run(cmd: list[str], cwd: Optional[str] = None) -> str:
    """Run a shell command and return its stdout. Raises on failure."""
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=cwd or ".",
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Command {' '.join(cmd)} failed (rc={result.returncode}):\n{result.stderr}"
        )
    return result.stdout.strip()


def get_diff(base_branch: str = "main", cwd: Optional[str] = None) -> str:
    """Return the unified diff of the current branch against *base_branch*."""
    return _run(["git", "diff", base_branch], cwd=cwd)


def get_range_diff(commit_range: str, cwd: Optional[str] = None) -> str:
    """Return the diff for a commit range like HEAD~3..HEAD."""
    return _run(["git", "diff", commit_range], cwd=cwd)


def get_staged_diff(cwd: Optional[str] = None) -> str:
    """Return the diff of staged (indexed) changes."""
    return _run(["git", "diff", "--cached"], cwd=cwd)


def get_log(
    base_branch: str = "main",
    max_commits: int = 20,
    cwd: Optional[str] = None,
) -> str:
    """Return a concise commit log since the branch diverged from *base_branch*."""
    return _run(
        [
            "git",
            "log",
            f"{base_branch}..HEAD",
            f"--max-count={max_commits}",
            "--oneline",
            "--no-decorate",
        ],
        cwd=cwd,
    )


def get_current_branch(cwd: Optional[str] = None) -> str:
    """Return the name of the current branch."""
    return _run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=cwd)


def read_file(path: str, cwd: Optional[str] = None) -> str:
    """Read a file's contents from the working tree."""
    full = Path(cwd or ".") / path
    return full.read_text()


def list_changed_files(base_branch: str = "main", cwd: Optional[str] = None) -> list[str]:
    """Return a list of files changed relative to *base_branch*."""
    output = _run(["git", "diff", "--name-only", base_branch], cwd=cwd)
    return [f for f in output.splitlines() if f]
