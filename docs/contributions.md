# Developer Contributions

This document details the responsibilities and deliverables fulfilled by each team member for the **Campus Helpdesk Ticket Management System** project.

---

## 👤 Keshan
**Role:** Project Lead & Database Developer

### Responsibilities
- Planned the repository structures and starter configurations.
- Defined and tested the MySQL database connection pool inside `database.py`.
- Formulated the database schema (`schema.sql`) and initialized default demo records.
- Configured the main FastAPI entrypoint `main.py`, managing routers inclusion and static files mounting.
- Reviewed and integrated features from teammates, resolving code and route integration conflicts.

### Deliverables
- [main.py](file:///d:/C%20Clarke/campus-helpdesk/main.py)
- [database.py](file:///d:/C%20Clarke/campus-helpdesk/database.py)
- [schema.sql](file:///d:/C%20Clarke/campus-helpdesk/schema.sql)
- [requirements.txt](file:///d:/C%20Clarke/campus-helpdesk/requirements.txt)

---

## 👤 AkilaKasun
**Role:** Create & View Backend Developer

### Responsibilities
- Implemented dashboard metrics retrieval (`get_ticket_counts`) for the main home page.
- Created read queries for fetching all tickets (`get_all_tickets`) and querying a ticket by its ID (`get_ticket_by_id`).
- Programmed backend validation checks for name, email format, category, and priority selections.
- Developed core submission routing, inserting validated records (`create_ticket`) into the database.

### Deliverables
- [crud_tickets_read.py](file:///d:/C%20Clarke/campus-helpdesk/crud_tickets_read.py)
- [routers/tickets_view.py](file:///d:/C%20Clarke/campus-helpdesk/routers/tickets_view.py)

---

## 👤 IsiwaraKumarage8
**Role:** Edit, Status & Delete Backend Developer

### Responsibilities
- Wrote database write operations for updating all editable fields (`update_ticket`) including the status.
- Designed status transition route processing (`update_status`) to modify a ticket's status on details view.
- Coded the ticket deletion function (`delete_ticket`) executing clean DELETE MySQL operations.
- Handled edge cases for invalid ticket IDs by returning custom 404 response templates.

### Deliverables
- [crud_tickets_write.py](file:///d:/C%20Clarke/campus-helpdesk/crud_tickets_write.py)
- [routers/tickets_manage.py](file:///d:/C%20Clarke/campus-helpdesk/routers/tickets_manage.py)

---

## 👤 neeprogrammer
**Role:** HTML & Jinja2 Template Developer

### Responsibilities
- Established the base layout skeleton structure (`base.html`) and responsive app shell.
- Built dashboard visuals, forms, lists, details view, edit/delete confirms, and error pages using Jinja2 templating syntax.
- Integrated backend context variables (e.g. ticket counts, lists, errors) dynamically.
- Formulated form POST fields matching FastAPI backend form-parameters expectations.

### Deliverables
- [templates/base.html](file:///d:/C%20Clarke/campus-helpdesk/templates/base.html)
- [templates/index.html](file:///d:/C%20Clarke/campus-helpdesk/templates/index.html)
- [templates/ticket_list.html](file:///d:/C%20Clarke/campus-helpdesk/templates/ticket_list.html)
- [templates/ticket_create.html](file:///d:/C%20Clarke/campus-helpdesk/templates/ticket_create.html)
- [templates/ticket_details.html](file:///d:/C%20Clarke/campus-helpdesk/templates/ticket_details.html)
- [templates/ticket_edit.html](file:///d:/C%20Clarke/campus-helpdesk/templates/ticket_edit.html)
- [templates/ticket_delete.html](file:///d:/C%20Clarke/campus-helpdesk/templates/ticket_delete.html)
- [templates/error.html](file:///d:/C%20Clarke/campus-helpdesk/templates/error.html)

---

## 👤 KomulHarana9
**Role:** CSS, Testing & Documentation Developer

### Responsibilities
- Designed and coded the responsive CSS layout stylesheet (`style.css`) using indigo-slate aesthetic color palettes.
- Styled badges for priorities and statuses, form inputs, buttons, tables, and alert dialogs.
- Performed end-to-end user-flow validation testing, verified form bounds, and resolved integration styles issues.
- Created execution instructions documentation in the project's README.

### Deliverables
- [static/css/style.css](file:///d:/C%20Clarke/campus-helpdesk/static/css/style.css)
- [README.md](file:///d:/C%20Clarke/campus-helpdesk/README.md)
