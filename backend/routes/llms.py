from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from LLM import ollama
router = APIRouter()

class QueryRequest(BaseModel):
    query: str

class ChromaData(BaseModel):
    content: str 

@router.get("/oll")
def func():
    return {"hello"}

@router.post("/ollama")
async def ask_ollama(request: QueryRequest):
    query_text = request.query.strip()
    if not query_text:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    answer = await ollama.ollama_answer(query_text)
    print(answer)
    latest_answer = answer
    return {"answer": answer}

@router.get("/chromadata")
async def show_all_data():
    documents = await ollama.get_from_collection()
    return {"documents":documents}

@router.post("/chromadata")
async def add_data(data: ChromaData):
    is_added = await ollama.add_to_collection(data.content)
    print(is_added)
    return{"status": is_added}