def normalize_trade(t: dict) -> dict:
    return {
        "side": t.get("side") or t.get("type", "UNKNOWN"),
        "title": (
            t.get("title")
            or t.get("market")
            or t.get("question")
            or "unknown"
        ),
        "size": float(t.get("size") or t.get("amount") or 0),

        "wallet": (
            t.get("wallet")
            or t.get("address")
            or t.get("user")
            or t.get("maker")
            or t.get("taker")
            or t.get("signer")
            or t.get("owner")
            or t.get("trader")
        ),

        "raw": t,
    }