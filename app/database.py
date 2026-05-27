# app/database.py

import sqlite3

DB_NAME = "polymarket.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        side TEXT,
        size REAL,
        wallet TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_trade(trade):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO trades (title, side, size, wallet)
    VALUES (?, ?, ?, ?)
    """, (
        trade.get("title"),
        trade.get("side"),
        float(trade.get("size", 0)),
        trade.get("wallet")
    ))

    conn.commit()
    conn.close()
