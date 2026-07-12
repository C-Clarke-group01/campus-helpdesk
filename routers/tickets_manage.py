"""
routers/tickets_manage.py
Edit / Status / Delete routes for the Campus Helpdesk Ticket Management System.
Owned by: Isiwara (IsiwaraKumarage8)
"""
from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from crud_tickets_write import (
    update_ticket,
    update_status,
    delete_ticket,
    get_ticket_by_id_for_manage,
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")

VALID_STATUSES = {"Open", "In Progress", "Resolved"}
VALID_PRIORITIES = {"Low", "Medium", "High"}
VALID_CATEGORIES = {"Technical", "Academic", "Finance", "Facilities", "Other"}


@router.get("/tickets/{ticket_id}/edit")
def edit_ticket_form(request: Request, ticket_id: int):
    ticket = get_ticket_by_id_for_manage(ticket_id)
    if ticket is None:
        return templates.TemplateResponse(
            request, "error.html",
            {"message": f"Ticket #{ticket_id} not found."},
            status_code=404,
        )
    return templates.TemplateResponse(request, "ticket_edit.html", {"ticket": ticket, "errors": []})


@router.post("/tickets/{ticket_id}/edit")
def edit_ticket_submit(
    request: Request,
    ticket_id: int,
    requester_name: str = Form(...),
    email: str = Form(...),
    category: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    priority: str = Form(...),
    status: str = Form(...),
):
    errors = []
    if not requester_name.strip():
        errors.append("Requester Name cannot be empty.")
    if not email.strip():
        errors.append("Email cannot be empty.")
    if category not in VALID_CATEGORIES:
        errors.append("Invalid category selected.")
    if not title.strip():
        errors.append("Title cannot be empty.")
    if not description.strip():
        errors.append("Description cannot be empty.")
    if priority not in VALID_PRIORITIES:
        errors.append("Invalid priority selected.")
    if status not in VALID_STATUSES:
        errors.append("Invalid status selected.")

    if errors:
        submitted_ticket = {
            "id": ticket_id,
            "requester_name": requester_name,
            "email": email,
            "category": category,
            "title": title,
            "description": description,
            "priority": priority,
            "status": status,
        }
        return templates.TemplateResponse(
            request, "ticket_edit.html",
            {"ticket": submitted_ticket, "errors": errors},
            status_code=400,
        )

    data = {
        "requester_name": requester_name.strip(),
        "email": email.strip(),
        "category": category,
        "title": title.strip(),
        "description": description.strip(),
        "priority": priority,
        "status": status,
    }
    updated = update_ticket(ticket_id, data)
    if not updated:
        return templates.TemplateResponse(
            request, "error.html",
            {"message": f"Ticket #{ticket_id} not found."},
            status_code=404,
        )
    return RedirectResponse(url=f"/tickets/{ticket_id}", status_code=303)


@router.post("/tickets/{ticket_id}/status")
def change_status(request: Request, ticket_id: int, status: str = Form(...)):
    if status not in VALID_STATUSES:
        return templates.TemplateResponse(
            request, "error.html",
            {"message": f"Invalid status value: {status}"},
            status_code=400,
        )
    updated = update_status(ticket_id, status)
    if not updated:
        return templates.TemplateResponse(
            request, "error.html",
            {"message": f"Ticket #{ticket_id} not found."},
            status_code=404,
        )
    return RedirectResponse(url=f"/tickets/{ticket_id}", status_code=303)


@router.get("/tickets/{ticket_id}/delete")
def delete_ticket_confirm(request: Request, ticket_id: int):
    ticket = get_ticket_by_id_for_manage(ticket_id)
    if ticket is None:
        return templates.TemplateResponse(
            request, "error.html",
            {"message": f"Ticket #{ticket_id} not found."},
            status_code=404,
        )
    return templates.TemplateResponse(request, "ticket_delete.html", {"ticket": ticket})


@router.post("/tickets/{ticket_id}/delete")
def delete_ticket_submit(request: Request, ticket_id: int):
    deleted = delete_ticket(ticket_id)
    if not deleted:
        return templates.TemplateResponse(
            request, "error.html",
            {"message": f"Ticket #{ticket_id} not found."},
            status_code=404,
        )
    return RedirectResponse(url="/tickets", status_code=303)