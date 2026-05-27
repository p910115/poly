# app/filter.py

from app.keywords import ALLOWED_KEYWORDS, BLOCKED_KEYWORDS


def normalize(text: str) -> str:
    return (text or "").lower()


def is_blocked(text: str) -> bool:
    text = normalize(text)
    return any(k.lower() in text for k in BLOCKED_KEYWORDS)


def is_allowed(text: str) -> bool:
    text = normalize(text)
    return any(k.lower() in text for k in ALLOWED_KEYWORDS)


def is_allowed_trade(trade: dict) -> bool:
    """
    Final gate:
    1. 先 blacklist（絕對禁止）
    2. 再 whitelist（至少命中一個）
    """
    title = trade.get("title", "")
    slug = trade.get("eventSlug", "")

    text = f"{title} {slug}".lower()

    if is_blocked(text):
        return False

    return is_allowed(text)