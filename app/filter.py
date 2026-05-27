from app.config import ALLOWED_KEYWORDS, BLOCKED_KEYWORDS

def is_allowed_trade(trade: dict) -> bool:
    title = trade.get("title", "").lower()

    if any(b.lower() in title for b in BLOCKED_KEYWORDS):
        return False

    return any(a.lower() in title for a in ALLOWED_KEYWORDS)