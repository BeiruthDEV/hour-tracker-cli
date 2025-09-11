from tracker.db import get_connection, init_db

def start_session(task: str):
    """Inicia uma nova sessão de trabalho para a task informada."""
    init_db()  # garante que a tabela existe
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO sessions (task, start_time) VALUES (?, datetime('now'))",
        (task,),
    )
    conn.commit()
    conn.close()
    print(f"✅ Sessão iniciada para tarefa: {task}")

def stop_session():
    """Finaliza a última sessão aberta (sem end_time)."""
    init_db()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE sessions SET end_time = datetime('now') WHERE end_time IS NULL"
    )
    conn.commit()
    conn.close()
    print("🛑 Sessão encerrada com sucesso.")

def report_sessions():
    """Exibe um relatório das sessões registradas."""
    init_db()
    conn = get_connection()
    cur = conn.cursor()
    rows = cur.execute(
        """
        SELECT id, task, start_time, end_time,
               ROUND((julianday(end_time) - julianday(start_time)) * 24, 2) AS hours
        FROM sessions
        ORDER BY start_time DESC
        """
    ).fetchall()
    conn.close()

    print("\n📊 Relatório de Sessões\n")
    for row in rows:
        print(f"ID: {row[0]} | Tarefa: {row[1]} | Início: {row[2]} | Fim: {row[3]} | Horas: {row[4]}")
