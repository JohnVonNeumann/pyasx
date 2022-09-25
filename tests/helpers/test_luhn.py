import pytest

from pyasx.helpers.luhn import  Luhn


@pytest.fixture
def valid_luhn_checksum():
    checksum: str = '10300000068413'
    luhn: Luhn = Luhn(checksum=checksum)
    return luhn

@pytest.fixture
def invalid_luhn_checksum():
    checksum: str = '10300000068419'
    luhn: Luhn = Luhn(checksum=checksum)
    return luhn


def test_repr(valid_luhn_checksum) -> None:
    assert repr(valid_luhn_checksum) == 'Luhn(checksum=10300000068413)'


def test_str(valid_luhn_checksum) -> None:
    assert str(valid_luhn_checksum) == 'Luhn=10300000068413'


def test_checksum_invalid(invalid_luhn_checksum) -> None:
    assert invalid_luhn_checksum.is_valid is False


def test_get_payload(valid_luhn_checksum):
    assert valid_luhn_checksum.payload == '1030000006841'


def test_get_check_digit(valid_luhn_checksum):
    assert valid_luhn_checksum.check_digit == 3


def test_validate(valid_luhn_checksum):
    assert valid_luhn_checksum.validate() is True


def test_transpose_isin_to_luhn_checksum_correct():
    checksum: str = Luhn.transpose_isin_to_luhn_checksum(isin='AU0000068413')
    assert checksum == '10300000068413'
