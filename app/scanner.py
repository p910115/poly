def print_trades(trades):
    for t in trades:
        side = t.get("side", "UNKNOWN")
        title = t.get("title", "UNKNOWN")
        size = t.get("size", 0)
        wallet = t.get("wallet", "unknown")

        print(
            f"[{side}] {title} | size: {size} | wallet: {wallet}"
        )