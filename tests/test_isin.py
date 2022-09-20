import pytest

from pyasx.isin import ISIN


def test_country_code():
    isin = ISIN(isin='AU0000068413')
    assert isin.country_code == 'AU'


def test_check_digit():
    isin = ISIN(isin='AU0000068413')
    assert isin.check_digit == '3'


def test_security_identifier():
    isin = ISIN(isin='AU0000068413')
    assert isin.security_identifier == '000006841'


def test_isin_length_validation():
    with pytest.raises(ValueError):
        ISIN(isin='XX012345678')


def test_isin_string_representation():
    isin = ISIN(isin='AU0000068413')
    assert str(repr(isin)) == 'ISIN(isin=AU0000068413)'


def test_isin_print_representation():
    isin = ISIN(isin='AU0000068413')
    assert str(isin) == 'ISIN=AU0000068413'


def test_isin_successful_validation():
    isin = ISIN(isin='AU0000068413')
    assert isin.validate() is True


def test_isin_failed_validation():
    isin = ISIN(isin='AU0000068418')
    assert isin.validate() is False
