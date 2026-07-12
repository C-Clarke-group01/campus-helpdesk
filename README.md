# Campus Helpdesk Ticket Management System

A web-based support ticket management system built using **FastAPI**, **MySQL**, and **Jinja2 templates** with a custom-crafted premium responsive **CSS** user interface. Designed for students and staff to submit support requests, and for helpdesk staff to view, update status, edit, and delete tickets.

---

## 🚀 Features

- **Responsive Dashboard**: Summary metrics for Total, Open, and Resolved tickets.
- **Ticket Submission Form**: Field validation (Presence, Email format, valid Priority, and Category options).
- **Ticket Table View**: Ordered list displaying complete ticket summaries and status/priority color badges.
- **Detailed Ticket Profile**: View full ticket descriptions, submitter metadata, and inline status updates.
- **Full CRUD Management**: Edit any aspect of tickets or confirm deletion via custom validation templates.
- **Error Handling**: Dedicated custom error views to gracefully handle invalid records or connectivity failures.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.x, FastAPI, Uvicorn
- **Database**: MySQL (using `mysql-connector-python`)
- **Frontend**: HTML5, Jinja2 Templates, Vanilla CSS3 (Custom design system - no Javascript)
- **Configuration**: `python-dotenv` for database environment variables

---

## 📋 Prerequisites & Installation

### 1. Database Setup

Ensure MySQL Server is running locally.

1. Connect to your MySQL shell:
   ```bash
   mysql -u root -p
   ```
2. Import the schema script:
   ```sql
   source schema.sql;
   ```

### 2. Project Installation

1. Clone the repository and navigate into the root directory.
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   ```
   - **Windows (PowerShell)**: `.venv\Scripts\Activate.ps1`
   - **macOS/Linux**: `source .venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Environment Variables Configuration

Create a `.env` file in the root folder (or edit the existing one) with your MySQL credentials:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=campus_helpdesk
```

---

## ⚙️ Running the Application

Start the local development server:
```bash
uvicorn main:app --reload
```

Visit the application at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🗺️ Routes Implemented

| Method | Route | Function |
| :--- | :--- | :--- |
| **GET** | `/` | Display the dashboard and metrics |
| **GET** | `/tickets` | Display all submitted tickets |
| **GET** | `/tickets/new` | Display the ticket submission form |
| **POST**| `/tickets/new` | Create/validate and save a new ticket |
| **GET** | `/tickets/{ticket_id}` | Display details of a specific ticket |
| **GET** | `/tickets/{ticket_id}/edit` | Display the ticket edit form |
| **POST**| `/tickets/{ticket_id}/edit` | Save edited fields to the database |
| **POST**| `/tickets/{ticket_id}/status`| Update only a ticket's status |
| **GET** | `/tickets/{ticket_id}/delete`| Display delete confirmation page |
| **POST**| `/tickets/{ticket_id}/delete`| Permanently delete a ticket |

---

## 👥 Individual Contribution Details

This project was built collectively by:
- **Keshan (Project Lead & Database Developer)**: Setup database schema, connection configurations, main router coordination, and final integration.
- **AkilaKasun (Create & View Backend Developer)**: Developed ticket creation backend logic, dashboard counts retrieval, and ticket display views.
- **IsiwaraKumarage8 (Edit, Status & Delete Backend Developer)**: Developed ticket updates, deletion routes, status change posts, and invalid ID error page handler.
- **neeprogrammer (HTML & Jinja2 Template Developer)**: Created all Jinja2 pages (Home, List, Details, Create, Edit, Delete, Error) matching the fields and variables.
- **KomulHarana9 (CSS, Testing & Documentation Developer)**: Developed the premium custom styling sheets (`style.css`), did end-to-end user-flow validation, and prepared documentation.
