CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project TEXT NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT,
    duration REAL
);
