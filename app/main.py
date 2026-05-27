import asyncio

from app.polymarket import fetch_recent_trades
from app.scanner import filter_recent_trades, print_trades
from app.wallet_db import (
    load_wallet_db,
    update_wallet_stats,
    print_top_wallets
)


# ============================================================
# MAIN
# ============================================================

async def main():

    # ========================================================
    # LOAD DB
    # ========================================================

    wallet_db = load_wallet_db()

    # ========================================================
    # FETCH TRADES
    # ========================================================

    trades = await fetch_recent_trades()

    if not trades:
        print("No trades fetched.")
        return

    # ========================================================
    # FILTER
    # ========================================================

    filtered = filter_recent_trades(
        trades=trades,
        min_size=1
    )

    # ========================================================
    # PRINT
    # ========================================================

    print_trades(filtered)

    # ========================================================
    # UPDATE DB
    # ========================================================

    update_wallet_stats(
        wallet_db=wallet_db,
        trades=filtered
    )

    # ========================================================
    # PRINT TOP WALLETS
    # ========================================================

    print_top_wallets(
        wallet_db=wallet_db,
        top_n=10
    )


# ============================================================
# ENTRY
# ============================================================

if __name__ == "__main__":
    asyncio.run(main())