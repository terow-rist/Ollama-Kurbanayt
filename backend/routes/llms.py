from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.database import db
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

class QueryRequest(BaseModel):
    username: str
    query: str

@router.post("/ollama")
async def handle_ollama(request: QueryRequest):
    query_text = request.query.strip()
    username = request.username  

    if not query_text:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    user_history = await db.history.find_one({"user_id": username})

    if not user_history:
        history_data = {"user_id": username, "chat": []}
        await db.history.insert_one(history_data)

    answer = await ollama.ollama_answer(query_text)
    
    story = {"user": query_text, "AI": answer}
    await db.history.update_one({"user_id": username}, {"$push": {"chat": story}})

    return {"answer": answer}
