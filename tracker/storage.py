import sqlite3
from datetime import datetime


DB_FILE = "hourtracker.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS time_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_start(project: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO time_entries (project, start_time) VALUES (?, ?)",
        (project, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


def stop(project: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE time_entries
        SET end_time = ?
        WHERE project = ? AND end_time IS NULL
    """, (datetime.now().isoformat(), project))
    conn.commit()
    conn.close()


def fetch_entries():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT project, start_time, end_time FROM time_entries")
    rows = cursor.fetchall()
    conn.close()
    return rows
