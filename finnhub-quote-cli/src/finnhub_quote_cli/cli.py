
import argparse

import requests

from finnhub_quote_cli.client import get_quote


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch a stock quote from Finnhub."
    )
    parser.add_argument(
        "symbol",
        help="Stock symbol to look up, for example NVDA",
    )
    args = parser.parse_args()

    try:
        quote = get_quote(args.symbol)
    except (requests.RequestException, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")

    print(f"Stock: {args.symbol.strip().upper()}")
    print(f"Current price: {quote['c']:.2f}")
    print(f"Day high: {quote['h']:.2f}")
    print(f"Day low: {quote['l']:.2f}")
    print(f"Opening price: {quote['o']:.2f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
