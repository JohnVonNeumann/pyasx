class Luhn(object):

    def __init__(self, *, checksum: str = None):
        self._checksum: str = checksum
        self._check_digit: int = self._get_check_digit()
        self._valid: bool = False

    def _get_check_digit(self) -> int:
        check_digit: int = int(self._checksum[-1])
        return check_digit

    @staticmethod
    def transpose_isin_to_luhn_checksum(*, isin: str = None) -> str:
        raise NotImplementedError


