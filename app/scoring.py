# app/scoring.py


def calculate_winrate(wins: int, total: int) -> float:
    if total == 0:
        return 0.0

    return wins / total



def calculate_wallet_score(
    pnl: float,
    winrate: float,
    total_trades: int,
    politics_ratio: float,
) -> float:

    score = 0.0

    # PnL contribution
    score += min(pnl / 1000, 30)

    # Winrate contribution
    score += winrate * 40

    # Activity contribution
    score += min(total_trades / 10, 20)

    # Political exposure penalty
    score -= politics_ratio * 100

    return round(score, 2)