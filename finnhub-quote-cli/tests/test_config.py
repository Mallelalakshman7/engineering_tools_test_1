
import pytest

from finnhub_quote_cli.config import get_api_key


def test_get_api_key_returns_configured_key(monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "test_api_key_123")

    assert get_api_key() == "test_api_key_123"


def test_get_api_key_rejects_missing_key(monkeypatch):
    monkeypatch.delenv("FINNHUB_API_KEY", raising=False)

    with pytest.raises(ValueError, match="FINNHUB_API_KEY is missing"):
        get_api_key()


def test_get_api_key_rejects_template_placeholder(monkeypatch):
    monkeypatch.setenv(
        "FINNHUB_API_KEY",
        "your_finnhub_api_key_here",
    )

    with pytest.raises(ValueError, match="template placeholder"):
        get_api_key()
