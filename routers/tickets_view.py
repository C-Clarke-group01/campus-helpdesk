from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import os

from database import get_db
import crud_tickets_read

tickets_router = APIRouter()
templates = Jinja2Templates(directory="templates")

VALID_CATEGORIES = {"Technical", "Academic", "Finance", "Facilities", "Other"}
VALID_PRIORITIES = {"Low", "Medium", "High"}


@tickets_router.get("/")
def home_page(request: Request):
    """GET / : Home page with dashboard counts"""
    db = get_db()
    try:
        counts = crud_tickets_read.get_ticket_counts(db)
    finally:
        db.close()

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "total": counts.get("total", 0),
            "open_count": counts.get("open", 0),
            "resolved": counts.get("resolved", 0)
        }
    )


@tickets_router.get("/tickets")
def list_tickets(request: Request):
    """GET /tickets : List all tickets"""
    db = get_db()
    tickets_list = []
    try:

        response_model = crud_tickets_read.get_all_tickets(db)


        if hasattr(response_model, 'data'):
            tickets_list = response_model.data
        elif isinstance(response_model, list):
            tickets_list = response_model
    finally:
        db.close()

    return templates.TemplateResponse(
        request,
        "ticket_list.html",
        {"tickets": tickets_list}
    )


@tickets_router.get("/tickets/new")
def show_new_ticket_form(request: Request):
    """GET /tickets/new : Show new ticket submission form"""
    return templates.TemplateResponse(
        request,
        "ticket_create.html",
        {"errors": [], "form_data": {}}
    )


@tickets_router.get("/tickets/{ticket_id}")
def show_ticket_details(request: Request, ticket_id: int):
    """GET /tickets/{ticket_id} : Show single ticket details"""
    db = get_db()
    try:
        ticket = crud_tickets_read.get_ticket_by_id(db, ticket_id)
    finally:
        db.close()

    if not ticket:

        return templates.TemplateResponse(
            request,
            "error.html",
            {"message": f"Ticket record #{ticket_id} could not be located."},
            status_code=404
        )


    return templates.TemplateResponse(
        request,
        "ticket_details.html",
        {"ticket": ticket}
    )


@tickets_router.post("/tickets/new")
def save_new_ticket(
        request: Request,
        requester_name: str = Form(...),
        email: str = Form(...),
        category: str = Form(...),
        title: str = Form(...),
        description: str = Form(...),
        priority: str = Form(...)
):
    """POST /tickets/new : Backend Form validation & insertion"""
    form_data = {
        "requester_name": requester_name.strip(),
        "email": email.strip(),
        "category": category.strip(),
        "title": title.strip(),
        "description": description.strip(),
        "priority": priority.strip()
    }

    errors = []
    # Essential Presence Checks
    for field, val in form_data.items():
        if not val:
            errors.append(f"{field.replace('_', ' ').capitalize()} field is required.")

    # Options Verification
    if form_data["category"] not in VALID_CATEGORIES:
        errors.append("Invalid option chosen for Category.")
    if form_data["priority"] not in VALID_PRIORITIES:
        errors.append("Invalid option chosen for Priority.")

    if errors:

        return templates.TemplateResponse(
            request,
            "ticket_create.html",
            {"errors": errors, "form_data": form_data}
        )

    db = get_db()
    try:
        response_model = crud_tickets_read.create_ticket(db, form_data)


        if response_model and (hasattr(response_model, 'status_code') or isinstance(response_model, dict)):
            status_code = getattr(response_model, 'status_code', response_model.get('status_code', 200))
            if status_code >= 400:
                msg = getattr(response_model, 'message', response_model.get('message', 'Database error.'))
                errors.append(msg)


                return templates.TemplateResponse(
                    request,
                    "ticket_create.html",
                    {"errors": errors, "form_data": form_data}
                )
    except Exception as e:
        errors.append(str(e))
        return templates.TemplateResponse(
            request,
            "ticket_create.html",
            {"errors": errors, "form_data": form_data}
        )
    finally:
        db.close()

    return RedirectResponse(url="/tickets", status_code=303)