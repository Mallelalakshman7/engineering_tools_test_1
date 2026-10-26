# Finnhub Quote CLI

A simple Python command-line application that retrieves stock quote information from the Finnhub API.

## Features

- Fetches stock quotes for a specified ticker symbol.
- Displays the current price, daily high, daily low, and opening price.
- Loads the Finnhub API key from a local `.env` file.
- Validates configuration and handles API errors.
- Uses `uv` for dependency management and packaging.

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)
- A Finnhub API key

## Setup

Clone or download the project, navigate to its root directory, and install the dependencies:

```bash
uv sync
```

Create a local `.env` file in the project root using `.env.template` as a reference:

```text
FINNHUB_API_KEY=your_actual_api_key
```

Replace the example value with your own Finnhub API key. Do not commit your `.env` file or share your API key.

## Usage

Run the CLI with a stock ticker symbol:

```bash
uv run finnhub-quote NVDA
```

The command displays the stock's current price, daily high, daily low, and opening price.

## Dependencies

- `requests` — HTTP requests to the Finnhub API.
- `python-dotenv` — Loads environment variables from `.env`.

## API

This project uses the Finnhub stock quote endpoint:

`https://finnhub.io/api/v1/quote`

## License

This project is provided for educational purposes.