# app/wallet/aggregator.py

from app.wallet.store import add_trade


def ingest_trades(trades: list):
    for t in trades:
        wallet = t.get("proxyWallet")
        if not wallet:
            continue
        add_trade(wallet, t)