from llama_index.core import SummaryIndex, Document, Settings

def get_recommendation_engine():
    # Mock user profile to simulate personalization logic
    user_context = [
        Document(text="User prefers eco-friendly shipping."),
        Document(text="User location: New York, USA.")
    ]
    index = SummaryIndex.from_documents(user_context)
    return index.as_query_engine(llm=Settings.llm)