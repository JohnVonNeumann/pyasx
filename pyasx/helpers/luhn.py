class Luhn(object):

    def __init__(self, *, checksum: str = None):
        self._checksum: str = checksum
        self._check_digit: int = self._get_check_digit()
        self._valid: bool = False

    def __repr__(self) -> str:
        return f'Luhn(checksum={self._checksum})'

    def _get_check_digit(self) -> int:
        print(self._checksum)
        check_digit: int = int(self._checksum[-1])
        print(check_digit)
        return check_digit

    @staticmethod
    def transpose_isin_to_luhn_checksum(*, isin: str = None) -> str:
        country_code = isin[0:1]
        return country_code

        raise NotImplementedError