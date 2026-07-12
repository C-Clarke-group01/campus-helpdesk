from mysql.connector import Error
from responses.response_model import SuccessResponseModel, ErrorResponseModel


def get_ticket_counts(db_connection):
    """Retrieves metrics for the dashboard home page."""
    cursor = db_connection.cursor(dictionary=True)
    counts = {"total": 0, "open": 0, "resolved": 0}
    try:
        # Total tickets
        cursor.execute("SELECT COUNT(*) as total FROM tickets;")
        counts["total"] = cursor.fetchone()["total"]

        # Open tickets
        cursor.execute("SELECT COUNT(*) as open FROM tickets WHERE status = 'Open';")
        counts["open"] = cursor.fetchone()["open"]

        # Resolved tickets
        cursor.execute("SELECT COUNT(*) as resolved FROM tickets WHERE status = 'Resolved';")
        counts["resolved"] = cursor.fetchone()["resolved"]
    finally:
        cursor.close()
    return counts

def get_all_tickets(db_connection):
    """Retrieves all tickets ordered by newest creation date."""
    cursor = db_connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM tickets ORDER BY id DESC;")
        tickets = cursor.fetchall()
    finally:
        cursor.close()
    return tickets


def get_ticket_by_id(db_connection, ticket_id: int):
    """Retrieves a single ticket by its ID."""
    cursor = db_connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM tickets WHERE id = %s;", (ticket_id,))
        ticket = cursor.fetchone()
    finally:
        cursor.close()
    return ticket



def create_ticket(db_connection, data: dict):
    """Persists a newly validated ticket into the MySQL database."""
    cursor = db_connection.cursor()
    query = """
        INSERT INTO tickets (requester_name, email, category, title, description, priority, status)
        VALUES (%s, %s, %s, %s, %s, %s, 'Open');
    """
    params = (
        data["requester_name"],
        data["email"],
        data["category"],
        data["title"],
        data["description"],
        data["priority"]
    )
    try:
        cursor.execute(query, params)
        db_connection.commit()
    finally:
        cursor.close()