import pytest

from pyasx.security import Security
from pyasx.isin import ISIN


@pytest.fixture
def valid_security() -> Security:
    security = Security(
        security_type='TEST ORDINARY SECURITY',
        isin=ISIN(
            isin='AU000000TES7'
        ),
        ticker='TES',
        company_name='TEST SECURITY'
    )
    return security


def test_security_security_type(valid_security):
    assert valid_security.security_type == 'TEST ORDINARY SECURITY'


def test_security_isin(valid_security):
    assert valid_security.isin == 'ISIN=AU000000TES7'


def test_security_ticker(valid_security):
    assert valid_security.ticker == 'TES'


def test_security_company_name(valid_security):
    assert valid_security.company_name == 'TEST SECURITY'


def test_security_invalid_ticker_length():
    with pytest.raises(ValueError):
        Security(
            security_type='TEST ORDINARY SECURITY',
            isin=ISIN(
                isin='AU000000TES7'
            ),
            ticker='TES1234',
            company_name='TEST SECURITY'
        )

    with pytest.raises(ValueError):
        Security(
            security_type='TEST ORDINARY SECURITY',
            isin=ISIN(
                isin='AU000000TES7'
            ),
            ticker='TE',
            company_name='TEST SECURITY'
        )
