"""
The Luhn.py module contains the Luhn class, which enables calculation of
Luhn checksum digits in order to verify the correctness of ISIN codes.

References can be found at:
    https://en.wikipedia.org/wiki/Luhn_algorithm
"""


class Luhn(object):
    """
    Represents a Luhn checksum.

    A luhn checksum is a checksum generated via the Luhn Algorithm.

    The Luhn algorithm is a simple checksum formula used to validate a
    variety of identification numbers, such as Credit Card numbers, IMEI
    numbers and a whole host of other items, including, as for our purposes,
    ISIN codes.
    """

    def __init__(self, *, checksum: str = None):
        self._checksum: str = checksum
        self._payload: str = self._get_payload()
        self._check_digit: int = self._get_check_digit()
        self._valid: bool = False

    def __repr__(self) -> str:
        return f'Luhn(checksum={self._checksum})'

    def __str__(self) -> str:
        return f'Luhn={self._checksum}'

    def _get_check_digit(self) -> int:
        check_digit: int = int(self._checksum[-1])
        return check_digit

    def _get_payload(self) -> str:
        payload: str = self._checksum[:-1]
        return payload

    def _compute_check_digit(self):
        """
        If the number already contains the check digit, drop that digit to form
        the "payload." The check digit is most often the last digit.
        With the payload, start from the rightmost digit.
        Moving left, double the value of every second digit (including the rightmost digit).
        Sum the digits of the resulting value in each position,
        using the original value where a digit did not get doubled in the previous step).
        The check digit is calculated by 10 − ( s mod 10 ).
        """
        digits = list(map(int, self._payload))
        odd_sum = sum(digits[-2::-2])
        even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-1::-2]])
        return 10 - ((odd_sum + even_sum) % 10)

    def validate(self) -> bool:
        """
        Uses the provided check digit, and then computes the check digit from
        the luhn checksum payload, and returns truth if they are the same.

        Returns:
            bool: Whether the provided checksum evaluates to the correct check digit.

        """
        computed_check_digit: int = self._compute_check_digit()
        if computed_check_digit == self._check_digit:
            return True
        else:
            return False

    @property
    def check_digit(self) -> int:
        return self._check_digit

    @property
    def payload(self) -> str:
        return self._payload

    @property
    def is_valid(self) -> bool:
        return self._valid

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
