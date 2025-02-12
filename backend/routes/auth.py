from fastapi import APIRouter, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
import os

router = APIRouter()

FRONTEND_DIR = "frontend"  # Directory where index.html is located
SIGNUP_FILE = os.path.join(FRONTEND_DIR, "signup.html")
LOGIN_FILE = os.path.join(FRONTEND_DIR, "login.html")
# Dummy user storage for demonstration purposes
users_db = {}

@router.get("/login", response_class=HTMLResponse)
async def login_page():
    with open(LOGIN_FILE, "r") as file:
        return HTMLResponse(content=file.read())

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username in users_db and users_db[username] == password:
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    raise HTTPException(status_code=400, detail="Invalid username or password")

@router.get("/signup", response_class=HTMLResponse)
async def signup_page():
    with open(SIGNUP_FILE, "r") as file:
        return HTMLResponse(content=file.read())

@router.post("/signup")
async def signup(username: str = Form(...), password: str = Form(...)):
    if username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[username] = password
    return RedirectResponse(url="/login", status_code=HTTP_303_SEE_OTHER)
