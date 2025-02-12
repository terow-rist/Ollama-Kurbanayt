from fastapi import FastAPI
from backend.routes.htmls import router as return_html
from backend.routes.auth import router as router_auth
from fastapi.staticfiles import StaticFiles




app = FastAPI()
app.include_router(return_html)
app.include_router(router_auth)
app.mount("/static", StaticFiles(directory="frontend"), name="static")
