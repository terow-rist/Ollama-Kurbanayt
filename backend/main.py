from fastapi import FastAPI
from backend.routes.htmls import router as return_html


app = FastAPI()
app.include_router(return_html)
