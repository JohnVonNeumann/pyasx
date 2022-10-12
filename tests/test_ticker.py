import pytest

from pyasx.ticker import Ticker, TickerType


@pytest.fixture
def valid_ticker() -> Ticker:
    ticker = Ticker(
        ticker='TES'
    )
    return ticker


def test_ticker_ticker(valid_ticker):
    assert valid_ticker.ticker == 'TES'


def test_ticker_type(valid_ticker):
    assert valid_ticker.ticker_type == TickerType.ORDINARY_SHARE
