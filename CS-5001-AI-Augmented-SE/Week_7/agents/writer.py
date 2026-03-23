def draft_content(plan: dict):
    """A2A: Receives Plan. Generates the final MD content."""
    prompt = f"Draft a {plan['item_type']} based on this justification: {plan['justification']}"
    content = chat_with_tools("You are a Writer.", prompt)
    return content # Passes to Gatekeeper