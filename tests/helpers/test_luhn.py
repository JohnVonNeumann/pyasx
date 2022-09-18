from pyasx.helpers import luhn


def test_repr() -> None:
    checksum: str = '10300000068413'
    luhn_cs: luhn.Luhn = luhn.Luhn(checksum=checksum)
    assert repr(luhn_cs) == 'Luhn(checksum=10300000068413)'


def test_str() -> None:
    checksum: str = '10300000068413'
    luhn_cs: luhn.Luhn = luhn.Luhn(checksum=checksum)
    assert str(luhn_cs) == 'Luhn=10300000068413'


def test_checksum_valid() -> None:
    checksum: str
    pass


def test_transpose_isin_to_luhn_checksum_correct():
    checksum: str = luhn.Luhn.transpose_isin_to_luhn_checksum(isin='AU0000068413')
    assert checksum == '10300000068413'
