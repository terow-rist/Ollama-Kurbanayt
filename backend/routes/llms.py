from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from LLM import ollama

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

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
    
    return {"answer": answer}
