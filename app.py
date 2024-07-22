import mesop as me
import mesop.labs as mel
from llama_index.core.query_engine import RetrieverQueryEngine

import settings
from models import llm
from retriever import CustomRetriever
from utils import index


@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/chat",
    title="P-graph Demo Chat",
)
def page():
    mel.chat(transform, title="P-graph", bot_user="P-graph bot")


custom_sub_retriever = CustomRetriever(
    index.property_graph_store,
    include_text=True,
    vector_store=index.vector_store,
    cohere_api_key=settings.COHERE_API_KEY,
)

query_engine = RetrieverQueryEngine.from_args(
    index.as_retriever(sub_retrievers=[custom_sub_retriever]), llm=llm
)


def transform(input: str, history: list[mel.ChatMessage]):
    response = query_engine.query(input)
    yield response.response
