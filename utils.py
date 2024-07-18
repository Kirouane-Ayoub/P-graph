from llama_index.core import PropertyGraphIndex, SimpleDirectoryReader
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore

import settings
from models import embed_model, llm

graph_store = Neo4jPropertyGraphStore(
    username=settings.NEW4J_USERNAME,
    password=settings.NEW4J_PASSWORD,
    url=settings.NEW4J_URL,
)

documents = SimpleDirectoryReader(settings.DATA_FOLDER).load_data()
index = PropertyGraphIndex.from_documents(
    documents,
    llm=llm,
    embed_model=embed_model,
    property_graph_store=graph_store,
    show_progress=True,
)
