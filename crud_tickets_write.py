"""
crud_tickets_write.py
Update / Delete database operations for the Campus Helpdesk Ticket Management System.
Owned by: Isiwara (IsiwaraKumarage8)

Kept separate from Akila's crud_tickets_read.py so we never edit the same file.
"""
from database import get_db
from mysql.connector import Error


def update_ticket(ticket_id: int, data: dict) -> bool:
    """
    Updates an existing ticket's editable fields.
    `data` must contain: requester_name, email, category, title, description, priority, status
    Returns True if a row was updated, False if ticket_id didn't exist.
    """
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(
            """
            UPDATE tickets
            SET requester_name = %s,
                email = %s,
                category = %s,
                title = %s,
                description = %s,
                priority = %s,
                status = %s
            WHERE id = %s
            """,
            (
                data["requester_name"],
                data["email"],
                data["category"],
                data["title"],
                data["description"],
                data["priority"],
                data["status"],
                ticket_id,
            ),
        )
        db.commit()
        return cursor.rowcount > 0
    except Error as e:
        db.rollback()
        print(f"[crud_tickets_write.py] Error updating ticket {ticket_id}: {e}")
        raise
    finally:
        cursor.close()
        db.close()


def update_status(ticket_id: int, new_status: str) -> bool:
    """
    Updates only the status field of a ticket.
    new_status must be one of: 'Open', 'In Progress', 'Resolved'
    Returns True if updated, False if ticket_id didn't exist.
    """
    valid_statuses = {"Open", "In Progress", "Resolved"}
    if new_status not in valid_statuses:
        raise ValueError(f"Invalid status: {new_status}")

    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(
            "UPDATE tickets SET status = %s WHERE id = %s",
            (new_status, ticket_id),
        )
        db.commit()
        return cursor.rowcount > 0
    except Error as e:
        db.rollback()
        print(f"[crud_tickets_write.py] Error updating status for ticket {ticket_id}: {e}")
        raise
    finally:
        cursor.close()
        db.close()


def delete_ticket(ticket_id: int) -> bool:
    """
    Deletes a ticket by id.
    Returns True if a row was deleted, False if ticket_id didn't exist.
    """
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM tickets WHERE id = %s", (ticket_id,))
        db.commit()
        return cursor.rowcount > 0
    except Error as e:
        db.rollback()
        print(f"[crud_tickets_write.py] Error deleting ticket {ticket_id}: {e}")
        raise
    finally:
        cursor.close()
        db.close()


def get_ticket_by_id_for_manage(ticket_id: int):
    """
    Fetches a single ticket — used to pre-fill the edit form and the delete
    confirmation page.

    NOTE: Once Akila's crud_tickets_read.py (get_ticket_by_id) is merged into
    main, you can switch your router to import that one instead of this and
    delete this function to avoid duplication. This exists so you can build
    and test your routes right now without waiting on his PR.
    """
    db = get_db()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM tickets WHERE id = %s", (ticket_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        db.close()