from collections import defaultdict


def rank_wallets(trades, top_n=10):
    wallet_volume = defaultdict(float)

    for t in trades:
        wallet = t.get("wallet", "unknown")
        size = float(t.get("size", 0))

        wallet_volume[wallet] += size

    ranked = sorted(
        wallet_volume.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_n]
