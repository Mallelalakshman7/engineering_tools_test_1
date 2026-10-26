
import pytest

from finnhub_quote_cli.client import get_quote


def test_get_quote_rejects_empty_symbol():
    with pytest.raises(ValueError, match="Stock symbol cannot be empty"):
        get_quote("")


def test_get_quote_rejects_whitespace_symbol():
    with pytest.raises(ValueError, match="Stock symbol cannot be empty"):
        get_quote("   ")