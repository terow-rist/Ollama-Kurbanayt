from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from backend.database import db

router = APIRouter()

@router.get("/history/{username}", response_class=HTMLResponse)
async def get_user_history(username: str):
    users_history = await db.history.find_one({"user_id": username})
    if not users_history:
        raise HTTPException(status_code="404", detail="Username has no history")
    
    history_html = "<ul>"
    for entry in users_history['chat']:
        history_html += f"<li><strong>User:</strong> {entry['user']} <br><strong>AI:</strong> {entry['AI']}</li>"
    history_html += "</ul>"


    return HTMLResponse(content=f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chat History</title>
    </head>
    <body>
        <h1>Chat History for {username}</h1>
        {history_html}
    </body>
    </html>
    """)