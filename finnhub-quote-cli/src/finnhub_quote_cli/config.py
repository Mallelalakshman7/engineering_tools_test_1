import os

from dotenv import load_dotenv

load_dotenv()


def get_api_key() -> str:
    """Return the Finnhub API key or raise a clear error."""
    api_key = os.getenv("FINNHUB_API_KEY", "").strip()

    if not api_key:
        raise ValueError(
            "FINNHUB_API_KEY is missing. Add it to your local .env file."
        )

    if api_key == "your_finnhub_api_key_here":
        raise ValueError(
            "FINNHUB_API_KEY still contains the template placeholder."
        )

    if api_key == "PASTE_YOUR_REAL_FINNHUB_KEY_HERE":
        raise ValueError(
            "Replace the placeholder in your local .env file with your API key."
        )

    return api_key