from dataclasses import dataclass
from agents.llm import chat_with_tools

@dataclass
class DiffReview:
    summary: str
    risk_level: str
    issues: list
    
def review_code(diff: str) -> DiffReview:
    """Analyzes code and passes analysis to the A2A chain."""
    system = "You are a Reviewer. Analyze the diff and provide a JSON summary."
    # MCP Tool: Reviewer could use a 'read_file' tool to get context if needed
    data = chat_with_tools(system, diff)
    return DiffReview(
        summary=data.get("summary", ""),
        risk_level=data.get("risk_level", "low"),
        issues=data.get("issues", [])
    )