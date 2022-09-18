class Luhn(object):

    def __init__(self, *, checksum: str = None):
        self._checksum: str = checksum
        self._check_digit: int = self._get_check_digit()
        self._valid: bool = False

    def __repr__(self) -> str:
        return f'Luhn(checksum={self._checksum})'

    def __str__(self) -> str:
        return f'Luhn=10300000068413'

    def _get_check_digit(self) -> int:
        check_digit: int = int(self._checksum[-1])
        return check_digit

    @staticmethod
    def transpose_isin_to_luhn_checksum(*, isin: str = None) -> list[int]:
        country_code: str = isin[0:2]
        converted_checksum: list[int] = []
        for char in country_code:
            ascii_code: int = ord(char) - 55
            converted_checksum.append(ascii_code)

        return converted_checksum
