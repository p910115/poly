from collections import defaultdict


def rank_wallets(trades, top_n=10):
    scores = defaultdict(float)

    for t in trades:
        wallet = t.get("wallet", "unknown")
        size = float(t.get("size", 0))

        if t.get("side") == "BUY":
            scores[wallet] += size
        else:
            scores[wallet] -= size * 0.5

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_n]