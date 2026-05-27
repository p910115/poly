# app/wallet/metrics.py

from app.wallet.store import get_wallet_trades


def compute_wallet_metrics(wallet: str):
    trades = get_wallet_trades(wallet)

    if not trades:
        return None

    total_trades = len(trades)

    total_size = sum(float(t.get("size", 0)) for t in trades)

    crypto_keywords = ["bitcoin", "btc", "ethereum", "eth", "solana", "sol"]

    crypto_count = 0
    blocked_count = 0

    for t in trades:
        text = (t.get("title", "") + t.get("eventSlug", "")).lower()

        if any(k in text for k in crypto_keywords):
            crypto_count += 1

    crypto_ratio = crypto_count / total_trades

    avg_size = total_size / total_trades

    return {
        "wallet": wallet,
        "total_trades": total_trades,
        "total_size": total_size,
        "avg_size": avg_size,
        "crypto_ratio": crypto_ratio,
    }