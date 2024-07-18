from typing import Any, Optional, Union

from llama_index.core.embeddings import BaseEmbedding
from llama_index.core.llms import LLM
from llama_index.core.prompts import PromptTemplate
from llama_index.core.retrievers import (
    CustomPGRetriever,
    TextToCypherRetriever,
    VectorContextRetriever,
)
from llama_index.core.vector_stores.types import VectorStore
from llama_index.postprocessor.cohere_rerank import CohereRerank


class CustomRetriever(CustomPGRetriever):
    def init(
        self,
        ## vector context retriever params
        embed_model: Optional[BaseEmbedding] = None,
        vector_store: Optional[VectorStore] = None,
        similarity_top_k: int = 4,
        path_depth: int = 1,
        ## text-to-cypher params
        llm: Optional[LLM] = None,
        text_to_cypher_template: Optional[Union[PromptTemplate, str]] = None,
        ## cohere reranker params
        cohere_api_key: Optional[str] = None,
        cohere_top_n: int = 2,
        **kwargs: Any,
    ) -> None:
        self.vector_retriever = VectorContextRetriever(
            self.graph_store,
            include_text=self.include_text,
            embed_model=embed_model,
            vector_store=vector_store,
            similarity_top_k=similarity_top_k,
            path_depth=path_depth,
        )

        self.cypher_retriever = TextToCypherRetriever(
            self.graph_store, llm=llm, text_to_cypher_template=text_to_cypher_template
        )

        self.reranker = CohereRerank(api_key=cohere_api_key, top_n=cohere_top_n)

    def custom_retrieve(self, query_str: str) -> str:
        nodes_1 = self.vector_retriever.retrieve(query_str)
        nodes_2 = self.cypher_retriever.retrieve(query_str)
        reranked_nodes = self.reranker.postprocess_nodes(
            nodes_1 + nodes_2, query_str=query_str
        )

        ## TMP: please change
        final_text = "\n\n".join(
            [n.get_content(metadata_mode="llm") for n in reranked_nodes]
        )

        return final_text