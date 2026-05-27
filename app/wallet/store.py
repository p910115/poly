# app/wallet/store.py

from collections import defaultdict

wallet_db = defaultdict(list)


def add_trade(wallet: str, trade: dict):
    wallet_db[wallet].append(trade)


def get_wallet_trades(wallet: str):
    return wallet_db.get(wallet, [])


def get_all_wallets():
    return list(wallet_db.keys())