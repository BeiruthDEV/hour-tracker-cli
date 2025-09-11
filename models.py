from datetime import datetime
from db import get_connection, init_db

def start_session(project: str):
    now = datetime.now().isoformat()
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO sessions (project, start_time) VALUES (?, ?)",
            (project, now),
        )
        conn.commit()
    print(f"⏱️ Sessão iniciada para '{project}' às {now}")

def stop_session(project: str):
    now = datetime.now()
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id, start_time FROM sessions WHERE project = ? AND end_time IS NULL ORDER BY id DESC LIMIT 1",
            (project,),
        ).fetchone()
        if not row:
            print(f"⚠️ Nenhuma sessão ativa encontrada para '{project}'")
            return

        start_time = datetime.fromisoformat(row["start_time"])
        duration = round((now - start_time).total_seconds() / 3600, 2)

        conn.execute(
            "UPDATE sessions SET end_time = ?, duration = ? WHERE id = ?",
            (now.isoformat(), duration, row["id"]),
        )
        conn.commit()

    print(f"✅ Sessão finalizada para '{project}'. Duração: {duration}h")

def report_sessions():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT project, SUM(duration) as total FROM sessions GROUP BY project"
        ).fetchall()

        if not rows:
            print("📊 Nenhum dado encontrado.")
            return

        print("\n📊 Horas acumuladas por projeto:\n")
        for row in rows:
            print(f" - {row['project']}: {row['total']:.2f}h")
