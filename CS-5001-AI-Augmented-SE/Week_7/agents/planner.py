from agents.llm import chat_with_tools
from agents.reviewer import DiffReview

def plan_action(review: DiffReview):
    """A2A: Receives Reviewer output. Tooling: Uses MCP to check repo."""
    # Example MCP Tool definition
    mcp_tools = [{
        "type": "function",
        "function": {
            "name": "list_repo_labels",
            "description": "Get available GitHub labels via MCP"
        }
    }]
    
    prompt = f"Review Summary: {review.summary}. Decide: create_issue or create_pr?"
    plan_data = chat_with_tools("You are a Planner.", prompt, tools=mcp_tools)
    
    # If tool_calls exist, the orchestrator would execute 'list_repo_labels' here
    return plan_data