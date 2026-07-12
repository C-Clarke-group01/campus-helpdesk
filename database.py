"""
database.py
Handles the MySQL database connection for the Campus Helpdesk Ticket
Management System.

Usage in other files:
    from database import get_db

    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tickets")
    rows = cursor.fetchall()
    cursor.close()
    db.close()
"""

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()  # reads variables from .env into the environment

# ---- Database configuration ----

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "24588"),      # put your MySQL password here
    "database": os.getenv("DB_NAME", "campus_helpdesk"),
}


def get_db():
    """
    Creates and returns a new MySQL database connection.
    Call this inside each route/function that needs the database,
    and remember to close it when done.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"[database.py] Error connecting to MySQL: {e}")
        raise


def test_connection():
    """
    Quick standalone test — run this file directly to check
    that your database connection works before building routes.
    """
    try:
        conn = get_db()
        if conn.is_connected():
            print("✅ Successfully connected to MySQL database:", DB_CONFIG["database"])
            conn.close()
    except Error as e:
        print("❌ Connection failed:", e)


if __name__ == "__main__":
    test_connection()