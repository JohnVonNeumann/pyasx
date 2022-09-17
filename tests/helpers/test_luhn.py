from pyasx.helpers import luhn


def test_repr() -> None:
    checksum: str = '1030U0000068413'
    luhn_cs = luhn.Luhn(checksum=checksum)
    assert repr(luhn_cs) == 'Luhn(checksum=1030U0000068413)'
