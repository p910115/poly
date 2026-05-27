import requests


POLYMARKET_API = "https://data-api.polymarket.com/trades"


async def fetch_recent_trades():
    try:
        response = requests.get(
            POLYMARKET_API,
            params={"limit": 100},
            timeout=10
        )

        print("STATUS:", response.status_code)

        if response.status_code != 200:
            return []

        data = response.json()

        if not isinstance(data, list):
            return []

        return data

    except Exception as e:
        print("ERROR FETCHING TRADES:", e)
        return []

