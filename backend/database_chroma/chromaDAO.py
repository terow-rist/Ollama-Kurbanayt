import os
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import chromadb

def init_chroma():
    chroma_storage_path = os.path.join(os.getcwd(), "chroma_db")
    os.makedirs(chroma_storage_path, exist_ok=True)

    client = chromadb.PersistentClient(path=chroma_storage_path)

    model_name = "all-MiniLM-L6-v2"
    embedded_func = SentenceTransformerEmbeddingFunction(
        model_name=model_name
    )

    collection_name= "codes"
    try:
        collection = client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedded_func
        )
        print(f"ChromaDB collection '{collection_name}' initialized successfully.")
        return collection  
    except Exception as e:
        print(f"Error initializing ChromaDB: {e}")
        return None

chroma_collection = init_chroma()
