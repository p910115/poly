import asyncio
from collections import defaultdict

from app.polymarket import fetch_recent_trades
from app.scanner import print_trades

try:
    from app.wallet.scorer import rank_wallets
except Exception:
    rank_wallets = None


# =========================================================
# NORMALIZE TRADE
# =========================================================
def normalize_trade(t):
    return {
        "side": t.get("side", "UNKNOWN"),
        "title": t.get("title", "UNKNOWN"),
        "size": float(t.get("size", 0)),
        "wallet": (
            t.get("wallet")
            or t.get("proxyWallet")
            or t.get("user")
            or "unknown"
        ),
    }


# =========================================================
# SIMPLE SCORING
# =========================================================
def fallback_rank_wallets(trades, top_n=10):
    scores = defaultdict(float)

    for t in trades:
        wallet = t["wallet"]
        size = t["size"]

        if t["side"] == "BUY":
            scores[wallet] += size
        else:
            scores[wallet] -= size * 0.5

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked[:top_n]


# =========================================================
# MAIN
# =========================================================
async def main():
    raw = fetch_recent_trades()

    print("STATUS: 200")

    if not raw:
        print("No trades found")
        return

    trades = [normalize_trade(t) for t in raw]

    print("\n=== FILTERED TRADES ===\n")
    print_trades(trades)

    print("\n=== TOP WALLETS ===\n")

    if rank_wallets:
        try:
            top = rank_wallets(trades, top_n=10)
        except Exception:
            top = fallback_rank_wallets(trades)
    else:
        top = fallback_rank_wallets(trades)

    for wallet, score in top:
        print(wallet, round(score, 2))


if __name__ == "__main__":
    asyncio.run(main())