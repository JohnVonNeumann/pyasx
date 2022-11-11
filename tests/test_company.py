import pytest

from pyasx.company import Company
from pyasx.ticker import Ticker


@pytest.fixture()
def valid_ticker() -> Ticker:
    ticker = Ticker(
        ticker='TES'
    )
    return ticker


@pytest.fixture
def valid_company(valid_ticker) -> Company:
    company = Company(
        ticker=valid_ticker,
        name='TEST SECURITY'
    )
    return company


def test_security_security_type(valid_company):
    assert valid_company.ticker == 'TES'
