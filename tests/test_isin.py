import pytest

from pyasx.isin import ISIN


@pytest.fixture
def valid_isin():
    isin = ISIN(isin='AU0000068413')
    return isin

@pytest.fixture
def invalid_isin():
    isin = ISIN(isin='AU0000068234')
    return isin

def test_country_code(valid_isin):
    assert valid_isin.country_code == 'AU'


def test_check_digit(valid_isin):
    assert valid_isin.check_digit == '3'


def test_security_identifier(valid_isin):
    assert valid_isin.security_identifier == '000006841'


def test_isin_length_validation():
    with pytest.raises(ValueError):
        ISIN(isin='XX012345678')


def test_isin_string_representation(valid_isin):
    assert str(repr(valid_isin)) == 'ISIN(isin=AU0000068413)'


def test_isin_print_representation(valid_isin):
    assert str(valid_isin) == 'ISIN=AU0000068413'


def test_isin_successful_validation(valid_isin):
    assert valid_isin.validate() is True


def test_isin_failed_validation(invalid_isin):
    assert invalid_isin.validate() is False
