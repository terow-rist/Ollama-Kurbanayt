from fastapi import APIRouter,UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from backend.database import db
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

@router.get("/chromadata")
async def show_all_data():
    documents = await ollama.get_from_collection()
    return {"documents":documents}

@router.post("/chromadata")
async def add_data(data: ChromaData):
    is_added = await ollama.add_to_collection(data.content)
    print(is_added)
    return{"status": is_added}

@router.post("/addfile")
async def add_data(file: UploadFile = File(...)):
    extracted_text = await ollama.extract_documents_from_file(file) 
    is_added = await ollama.add_to_collection(extracted_text)
    return {"status": is_added}