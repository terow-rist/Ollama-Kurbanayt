from fastapi import FastAPI
from backend.routes.htmls import router as return_html
from backend.routes.llms import router as return_ollama


app = FastAPI()
app.include_router(return_html)
app.include_router(return_ollama)
