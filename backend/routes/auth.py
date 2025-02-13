from fastapi import APIRouter, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from backend.database import db
from starlette.status import HTTP_303_SEE_OTHER
import os

router = APIRouter()

FRONTEND_DIR = "frontend"  # Directory where index.html is located
SIGNUP_FILE = os.path.join(FRONTEND_DIR, "signup.html")
LOGIN_FILE = os.path.join(FRONTEND_DIR, "login.html")
# Dummy user storage for demonstration purposes

@router.get("/login", response_class=HTMLResponse)
async def login_page():
    with open(LOGIN_FILE, "r") as file:
        return HTMLResponse(content=file.read())

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    stored_user = await db.users.find_one({"username" : username})

    if stored_user and stored_user["password"] == password:
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    raise HTTPException(status_code=400, detail="Invalid username or password")

@router.get("/signup", response_class=HTMLResponse)
async def signup_page():
    with open(SIGNUP_FILE, "r") as file:
        return HTMLResponse(content=file.read())

@router.post("/signup")
async def signup(username: str = Form(...), password: str = Form(...)):
    existing_user = await db.users.find_one({"username": username})

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    user_data = {"username": username, "password": password}
    await db.users.insert_one(user_data)
    
    return RedirectResponse(url="/login", status_code=HTTP_303_SEE_OTHER)
