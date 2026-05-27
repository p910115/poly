import requests

URL = "https://data-api.polymarket.com/trades"


def fetch_recent_trades():
    try:
        response = requests.get(URL, timeout=10)

        if response.status_code != 200:
            print("API ERROR:", response.status_code)
            return []

        data = response.json()

        if isinstance(data, list):
            return data

        return data.get("history", [])

    except Exception as e:
        print("FETCH ERROR:", e)
        return []
