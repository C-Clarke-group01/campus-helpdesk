"""
main.py
Entry point for the Campus Helpdesk Ticket Management System.
Run with: uvicorn main:app --reload
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import get_db

app = FastAPI(title="Campus Helpdesk Ticket Management System")

# Serve CSS/JS/images from the static/ folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Point Jinja2 at the templates/ folder
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    """
    Home page — shows total/open/resolved ticket counts.
    (Counts are placeholder 0s for now; Developer 2 will wire in
    real queries using crud.py)
    """
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM tickets")
    total = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS open_count FROM tickets WHERE status='Open'")
    open_count = cursor.fetchone()["open_count"]

    cursor.execute("SELECT COUNT(*) AS resolved FROM tickets WHERE status='Resolved'")
    resolved = cursor.fetchone()["resolved"]

    cursor.close()
    db.close()

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "total": total,
            "open_count": open_count,
            "resolved": resolved,
        }
    )