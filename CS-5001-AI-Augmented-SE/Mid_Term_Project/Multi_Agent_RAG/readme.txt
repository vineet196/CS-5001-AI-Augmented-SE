 Multi-Agent Agentic RAG System

This project implements a sophisticated Multi-Agent Retrieval-Augmented Generation (RAG) system using LlamaIndex and Ollama. It is designed to act as an intelligent research and operations orchestrator that synthesizes information from structured databases, local research papers, and real-time web data.

---

Core Architecture

The system follows an Agentic RAG pattern where a Master Orchestrator (powered by qwen3:0.6b) decomposes user queries and delegates tasks to specialized sub-agents:

* SQL Agent: Queries a local SQLite database (`orders.db`) for structured technical metrics and project data.
* Semantic Agent: Searches a local directory (`/data`) containing PDFs and text files for deep scientific context using vector embeddings.
* Web Agent: Utilizes DuckDuckGo to fetch real-time news and global industry trends.
* Recommendation Agent: Personalizes responses based on user profiles (e.g., eco-friendly preferences).

---

# # Key Features

* 100% Local Execution: Runs entirely on your hardware using Ollama for both LLM inference and embeddings, ensuring data privacy.
* Interactive Terminal Interface: Features a non-hardcoded, asynchronous loop for real-time chatting with the agent.
* Sequential Reasoning: Uses a custom system prompt to prioritize internal "trusted" data over general web search results.
* Asynchronous Workflow: Built on the 2026 LlamaIndex `FunctionAgent` architecture for efficient task handling.

---

# # Installation & Setup

 1. Prerequisites

* Python 3.10+
* Ollama (Download and run `ollama serve`)

 2. Model Preparation

Pull the necessary models to your local machine:

```bash
ollama pull qwen3:0.6b
ollama pull nomic-embed-text

```

 3. Dependency Installation

Install the required Python packages:

```bash
pip install llama-index-core llama-index-agent-openai llama-index-llms-ollama llama-index-embeddings-ollama llama-index-tools-duckduckgo python-dotenv sqlalchemy

```

 4. Environment Configuration

Create a `.env` file in the root directory:

```text
OLLAMA_MODEL=qwen3:0.6b
OLLAMA_EMBED_MODEL=nomic-embed-text

```

---

# # Usage

1. Initialize Database: Run your database creation script to generate `orders.db`.
2. Add Research Data: Place your research papers (PDFs/Text) in the `./data` folder.
3. Launch System:
```bash
python app.py

```


4. Interact: Enter queries like: "The latest news on Bitcoin and the status of order 99.