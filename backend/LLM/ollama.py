from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from backend.database_chroma.chromaDAO import chroma_collection
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
import os
import tempfile



llm = Ollama(model="llama3.2", request_timeout=120.0)
model_name = "all-MiniLM-L6-v2"
async def add_to_collection(document):
    try:
        embedding = SentenceTransformer(model_name).encode(document).tolist()
        doc_id = f"doc_{len(chroma_collection.get()['ids']) + 1}"
        chroma_collection.add(documents=[document], embeddings=embedding, ids = [doc_id])
        return "added sucsefully"
    except Exception as e:
        return str(e) 
    
async def get_from_collection():
    try:
        documents = chroma_collection.get()["documents"]
        return documents
    except Exception as e:
        return str(e)
    
async def extract_documents_from_file(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_path = temp_file.name
            temp_file.write(await uploaded_file.read())  # Await file read
        
        loader = PyPDFLoader(temp_path)
        documents = loader.load()
        
        # Ensure cleanup
        os.remove(temp_path)  

        text_list = "\n".join([doc.page_content for doc in documents])
        return text_list
    except Exception as e:
        return str(e)

async def ollama_answer(user_query):
    system_instruction = (
        "You are a code generator AI. Always return only pure code without any explanations, "
        "comments, or extra text. If the user asks for HTML, return only HTML. "
        "If they ask for CSS, return only CSS. If they ask for JavaScript, return only JavaScript."
    )

    query_vector = SentenceTransformer(model_name).encode(user_query).tolist()

    results = chroma_collection.query(
        query_embeddings=query_vector,
        n_results=1,
        include=["embeddings", "documents"]
    )
    docs = ""
    for doc in results:
        docs += doc

    messages = [
        ChatMessage(role="system", content=system_instruction),
        ChatMessage(role="user", content=user_query),
        ChatMessage(role="assistant", content=docs),
    ]

    responce = ""
    try:        
        responce_stream = llm.stream_chat(messages=messages)

        for chunk in responce_stream:
            responce += chunk.delta
        return responce
    except Exception as e:
        return str(e)
        