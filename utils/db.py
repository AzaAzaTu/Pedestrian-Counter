import sqlite3
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parents[1]
DB_DIR = BASE_DIR / "database"
DB_PATH = DB_DIR / "history.db"


def init_db():
    DB_DIR.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            original_filename TEXT NOT NULL,
            upload_path TEXT NOT NULL,
            result_path TEXT NOT NULL,
            pedestrian_count INTEGER NOT NULL,
            confidence REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_request(original_filename, upload_path, result_path, pedestrian_count, confidence):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO requests (
            timestamp,
            original_filename,
            upload_path,
            result_path,
            pedestrian_count,
            confidence
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        original_filename,
        upload_path,
        result_path,
        pedestrian_count,
        confidence
    ))

    conn.commit()
    conn.close()


def get_history(limit=10):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM requests
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]
