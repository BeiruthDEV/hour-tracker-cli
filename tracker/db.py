import sqlite3

DB_NAME = "hourtracker.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        with open("schema.sql", "r", encoding="utf-8") as f:
            conn.executescript(f.read())
