import os  # <--- Add this line
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings

def get_semantic_engine():
    # Ensure the data directory exists
    if not os.path.exists("./data"):
        os.makedirs("./data")
        with open("./data/info.txt", "w") as f:
            f.write("Standard shipping takes 3-5 days. Express takes 1-2 days.")

    # Load documents from the local folder
    documents = SimpleDirectoryReader("./data").load_data()
    
    # Create a local index using Ollama (configured in app.py)
    index = VectorStoreIndex.from_documents(documents)
    return index.as_query_engine()