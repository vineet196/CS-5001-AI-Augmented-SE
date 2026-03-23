def verify_and_post(draft: dict):
    """The final gate. Uses MCP to write to the external system."""
    
    # Verify logic...
    is_safe = True 
    
    if is_safe:
        # MCP Tooling: The actual 'action' happens here
        github_tool = [{
            "type": "function",
            "function": {
                "name": "post_to_github",
                "parameters": {"title": draft['title'], "body": draft['body']}
            }
        }]
        return chat_with_tools("Post this content.", "Execute post_to_github", tools=github_tool)
    return "Safety Check Failed."