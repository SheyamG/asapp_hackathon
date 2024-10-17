# Embedding Function (updated)
from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function(model_name):
    embeddings = OllamaEmbeddings(model=model_name)
    return embeddings
