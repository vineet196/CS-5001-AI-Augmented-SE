import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

# Ollama settings — uses the OpenAI-compatible API at localhost:11434
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "devstral-2:123b-cloud")

# Maximum reflection/revision cycles before accepting the draft
MAX_REVISION_CYCLES = 3
