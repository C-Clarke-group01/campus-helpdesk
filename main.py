"""
main.py
Entry point for the Campus Helpdesk Ticket Management System.
Run with: uvicorn main:app --reload
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import get_db

from routers.tickets_view import tickets_router
from routers.tickets_manage import router as tickets_manage_router

app = FastAPI(title="Campus Helpdesk Ticket Management System")

# Serve CSS/JS/images from the static/ folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Point Jinja2 at the templates/ folder
templates = Jinja2Templates(directory="templates")


app.include_router(tickets_router)
app.include_router(tickets_manage_router)