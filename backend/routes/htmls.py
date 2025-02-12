from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
import os
router = APIRouter()

@router.get("/data", response_class=HTMLResponse)
async def return_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI HTML Response</title>
    </head>
    <body>
        <h1>Hello from FastAPI!</h1>
        <p>This is an HTML response from the FastAPI backend.</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

FRONTEND_DIR = "frontend"  # Directory where index.html is located
INDEX_FILE = os.path.join(FRONTEND_DIR, "index.html")

@router.get("/", response_class=FileResponse)
async def serve_index():
    if os.path.exists(INDEX_FILE):
        return FileResponse(INDEX_FILE)
    return {"error": "index.html not found"}
