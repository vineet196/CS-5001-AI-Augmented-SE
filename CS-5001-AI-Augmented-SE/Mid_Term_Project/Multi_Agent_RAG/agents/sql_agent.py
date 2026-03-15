from llama_index.core import SQLDatabase, Settings
from llama_index.core.query_engine import NLSQLTableQueryEngine
from sqlalchemy import create_engine

def get_sql_engine():
    # Connects to your local SQLite database
    engine = create_engine("sqlite:///orders.db")
    sql_database = SQLDatabase(engine, include_tables=["orders"])
    
    # Creates a query engine that translates Natural Language to SQL
    return NLSQLTableQueryEngine(
        sql_database=sql_database, 
        tables=["orders"],
        llm=Settings.llm
    )