# app/database.py

import aiosqlite
from config import DATABASE_PATH


CREATE_WALLET_TABLE = """
CREATE TABLE IF NOT EXISTS wallets (
    wallet TEXT PRIMARY KEY,
    total_trades INTEGER,
    wins INTEGER,
    losses INTEGER,
    pnl REAL,
    winrate REAL,
    score REAL,
    politics_ratio REAL,
    updated_at TEXT
)
"""


CREATE_TRADES_TABLE = """
CREATE TABLE IF NOT EXISTS trades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wallet TEXT,
    market_title TEXT,
    side TEXT,
    amount REAL,
    pnl REAL,
    timestamp TEXT
)
"""


async def init_db():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(CREATE_WALLET_TABLE)
        await db.execute(CREATE_TRADES_TABLE)
        await db.commit()