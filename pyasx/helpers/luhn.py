class Luhn(object):

    def __init__(self, *, checksum: str = None):
        self._checksum: str = checksum
        self._payload: str = self._get_payload()
        self._check_digit: int = self._get_check_digit()
        self._valid: bool = False

    def __repr__(self) -> str:
        return f'Luhn(checksum={self._checksum})'

    def __str__(self) -> str:
        return f'Luhn=10300000068413'

    def _get_check_digit(self) -> int:
        check_digit: int = int(self._checksum[-1])
        return check_digit

    def _get_payload(self) -> str:
        payload: str = self._checksum[:-1]
        return payload

    @property
    def check_digit(self) -> int:
        return self._check_digit

    @property
    def payload(self) -> str:
        return self._payload

    @staticmethod
    def transpose_isin_to_luhn_checksum(*, isin: str = None) -> str:
        """
        Accepts an ISIN as input and produces a Luhn checksum with the 2 alpha
        country code transposed to valid ASCII characters.

        Args:
            isin (str): A single ISIN code.

        Returns:
            str: An unvalidated Luhn checksum
        """
        country_code: str = isin[0:2]
        converted_checksum: list[str] = []
        for char in country_code:
            ascii_code: int = ord(char) - 55
            converted_checksum.append(str(ascii_code))

        converted_checksum.append(isin[2:])

        luhn_checksum = ''.join(converted_checksum)

        return luhn_checksum
