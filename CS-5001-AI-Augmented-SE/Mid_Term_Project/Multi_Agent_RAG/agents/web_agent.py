from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from llama_index.core.tools import FunctionTool

def get_web_tool():
    tool_spec = DuckDuckGoSearchToolSpec()
    
    # Use 'duckduckgo_full_search' as indicated by the AttributeError
    return FunctionTool.from_defaults(
        fn=tool_spec.duckduckgo_full_search,
        name="duckduckgo_search",
        description="Search the web for real-time information or public data."
    )