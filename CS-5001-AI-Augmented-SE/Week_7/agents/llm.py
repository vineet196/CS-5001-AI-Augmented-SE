"""Shared LLM calling helper — updated for MCP Tooling support."""
from __future__ import annotations
import json
from typing import Any, List, Dict
from openai import OpenAI
import config

_client = OpenAI(base_url=config.OLLAMA_BASE_URL, api_key="ollama")

def chat_with_tools(
    system_prompt: str,
    user_message: str,
    tools: List[Dict] = None,
    model: str = None
) -> Dict[str, Any]:
    """Executes a chat completion that supports MCP tool definitions."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]
    
    response = _client.chat.completions.create(
        model=model or config.OLLAMA_MODEL,
        messages=messages,
        tools=tools, # MCP Tools passed here
        tool_choice="auto" if tools else None
    )
    
    message = response.choices[0].message
    
    # If the LLM wants to use an MCP Tool
    if message.tool_calls:
        return {"tool_calls": message.tool_calls, "raw": message}
    
    # Otherwise return JSON content
    return json.loads(message.content)