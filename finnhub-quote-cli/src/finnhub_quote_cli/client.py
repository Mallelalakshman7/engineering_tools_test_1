import requests

from finnhub_quote_cli.config import get_api_key

API_URL = "https://finnhub.io/api/v1/quote"


def get_quote(symbol: str) -> dict:
    """Fetch a stock quote from Finnhub."""
    symbol = symbol.strip().upper()

    if not symbol:
        raise ValueError("Stock symbol cannot be empty.")

    headers = {
        "X-Finnhub-Token": get_api_key(),
        "Accept": "application/json",
    }

    params = {"symbol": symbol}

    response = requests.get(
        API_URL,
        headers=headers,
        params=params,
        timeout=10,
    )
    response.raise_for_status()

    quote = response.json()

    required_fields = ("c", "h", "l", "o")
    if not isinstance(quote, dict) or any(
        field not in quote for field in required_fields
    ):
        raise ValueError("Finnhub returned an unexpected quote response.")

    return quote