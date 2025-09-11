import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "hourtracker.db")
SCHEMA_FILE = os.path.join(os.path.dirname(__file__), "schema.sql")

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    """Cria as tabelas do banco caso ainda não existam."""
    conn = get_connection()
    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
