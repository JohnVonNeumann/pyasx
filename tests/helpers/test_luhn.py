from pyasx.helpers import luhn


def test_repr() -> None:
    checksum: str = '10300000068413'
    luhn_cs: luhn.Luhn = luhn.Luhn(checksum=checksum)
    assert repr(luhn_cs) == 'Luhn(checksum=10300000068413)'


def test_str() -> None:
    checksum: str = '10300000068413'
    luhn_cs: luhn.Luhn = luhn.Luhn(checksum=checksum)
    assert str(luhn_cs) == 'Luhn=10300000068413'


def test_checksum_invalid() -> None:
    checksum: str = '10300000068419'
    luhn_cs: luhn.Luhn = luhn.Luhn(checksum=checksum)
    assert luhn_cs.is_valid is False


def test_get_payload():
    checksum: str = '10300000068413'
    luhn_cs: luhn.Luhn = luhn.Luhn(checksum=checksum)
    assert luhn_cs.payload == '1030000006841'


def test_get_check_digit():
    checksum: str = '10300000068413'
    luhn_cs: luhn.Luhn = luhn.Luhn(checksum=checksum)
    assert luhn_cs.check_digit == 3


def test_transpose_isin_to_luhn_checksum_correct():
    checksum: str = luhn.Luhn.transpose_isin_to_luhn_checksum(isin='AU0000068413')
    assert checksum == '10300000068413'
