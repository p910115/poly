def filter_recent_trades(trades, min_size=1):
    filtered = []

    for t in trades:
        try:
            size = float(t.get("size", 0))

            if size >= min_size:
                filtered.append({
                    "title": t.get("title", "UNKNOWN"),
                    "side": t.get("side", "UNKNOWN"),
                    "size": size,
                    "wallet": (
                        t.get("proxyWallet")
                        or t.get("makerAddress")
                        or t.get("user")
                        or "unknown"
                    )
                })

        except Exception:
            continue

    return filtered


def print_trades(trades):
    for t in trades:
        print(
            f"[{t['side']}] "
            f"{t['title']} | "
            f"size: {t['size']} | "
            f"wallet: {t['wallet']}"
        )
