import json
import os


# ============================================================
# CONFIG
# ============================================================

DB_FILE = "wallet_db.json"


# ============================================================
# LOAD DB
# ============================================================

def load_wallet_db():

    if not os.path.exists(DB_FILE):
        return {}

    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)

    except Exception:
        return {}


# ============================================================
# SAVE DB
# ============================================================

def save_wallet_db(wallet_db):

    with open(DB_FILE, "w") as f:
        json.dump(wallet_db, f, indent=2)


# ============================================================
# UPDATE STATS
# ============================================================

def update_wallet_stats(wallet_db, trades):

    for trade in trades:

        wallet = trade.get("wallet", "unknown")
        size = float(trade.get("size", 0))

        if wallet not in wallet_db:

            wallet_db[wallet] = {
                "total_volume": 0,
                "trade_count": 0
            }

        wallet_db[wallet]["total_volume"] += size
        wallet_db[wallet]["trade_count"] += 1

    save_wallet_db(wallet_db)


# ============================================================
# PRINT TOP WALLETS
# ============================================================

def print_top_wallets(wallet_db, top_n=10):

    print("\n=== TOP WALLETS ===\n")

    sorted_wallets = sorted(
        wallet_db.items(),
        key=lambda x: x[1]["total_volume"],
        reverse=True
    )

    for wallet, stats in sorted_wallets[:top_n]:

        volume = round(stats["total_volume"], 2)

        print(f"{wallet} | volume={volume}")