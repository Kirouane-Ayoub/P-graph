from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM

import settings

llm = HuggingFaceLLM(model_name=settings.LLM_MODEL)
embed_model = HuggingFaceEmbedding(model_name=settings.EMBED_MODEL)
Settings.llm = llm
Settings.embed_model = embed_model
