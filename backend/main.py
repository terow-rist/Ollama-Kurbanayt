from fastapi import FastAPI
from backend.routes.htmls import router as return_html

from backend.routes.llms import router as return_ollama

from backend.routes.auth import router as router_auth
from fastapi.staticfiles import StaticFiles

from backend.routes.history import router as router_history


app = FastAPI()
app.include_router(return_html)

app.include_router(return_ollama)

app.include_router(router_auth)

app.include_router(router_history)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

