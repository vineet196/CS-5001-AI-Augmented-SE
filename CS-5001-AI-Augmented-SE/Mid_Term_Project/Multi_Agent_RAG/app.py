import os
import asyncio
from dotenv import load_dotenv

# Core LlamaIndex Imports
from llama_index.core import Settings
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata

# Ollama Connectors
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Import your local agents
from agents.sql_agent import get_sql_engine
from agents.semantic_agent import get_semantic_engine
from agents.web_agent import get_web_tool
from agents.recommend_agent import get_recommendation_engine

# Load environment variables
load_dotenv()

# 1. Configuration for Local Ollama
Settings.llm = Ollama(
    model=os.getenv("OLLAMA_MODEL", "qwen3:0.6b"), # Changed to a lighter model as requested
    request_timeout=360.0
)
Settings.embed_model = OllamaEmbedding(
    model_name=os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")
)

# 2. Register Specialized Tools
tools = [
    QueryEngineTool(
        query_engine=get_sql_engine(),
        metadata=ToolMetadata(name="sql_agent", description="Queries local SQL for order data.")
    ),
    QueryEngineTool(
        query_engine=get_semantic_engine(),
        metadata=ToolMetadata(name="doc_agent", description="Searches local PDFs for shipping policies.")
    ),
    get_web_tool(), 
    QueryEngineTool(
        query_engine=get_recommendation_engine(),
        metadata=ToolMetadata(name="rec_agent", description="Checks user profile for preferences.")
    )
]

# 3. Initialize the Master Agent
master_agent = FunctionAgent(
    name="Master_Orchestrator",
    tools=tools,
    llm=Settings.llm,
    system_prompt="You are an assistant that uses tools to answer queries step-by-step.",
)

# 4. Interactive Async Execution Loop
async def main():
    print(f"\n--- Multi-Agent RAG System Active ---")
    print(f"Model: {os.getenv('OLLAMA_MODEL')}")
    print("Type 'exit' or 'quit' to stop the program.\n")
    
    while True:
        # Get input from terminal
        user_query = input("User > ")
        
        # Check for exit command
        if user_query.lower() in ["exit", "quit"]:
            print("Shutting down agents... Goodbye!")
            break
        
        # Skip empty inputs
        if not user_query.strip():
            continue

        try:
            print(f"\n[Agent is thinking...]")
            
            # Use 'await' to run the agent with the dynamic prompt
            response = await master_agent.run(user_query)
            
            print(f"\nFINAL RESPONSE:\n{response}\n" + "-"*30)
            
        except Exception as e:
            print(f"\nCaught Error: {e}")

# 5. Start the Event Loop
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")