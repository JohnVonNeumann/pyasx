"""
The ISIN class provides all the functionality required to work with ISIN
codes at a basic level.

Reference on the format of valid ISINs:
    https://www.isin.org/isin-format/
"""


class ISIN(object):
    """
    Represents an ISIN code.

    An ISIN code is an International Securities Identification Number.
    It is used to identify a financial Security.

    The structure of an ISIN is made up of three components:

        1. An ISO 3166-1 alpha-2 two character code for the issuing country
        2. A nine-character alphanumeric security identifier
        3. A single check digit.

    Further Information:

        https://en.wikipedia.org/wiki/International_Securities_Identification_Number
    """
    def __init__(self, *, isin: str = None):
        """

        Args:
            isin: str
                An ISIN code.

        Raises:
            ValueError: On ISIN inputs that are not 12 characters long.
        """
        self._isin: str = isin
        self._security_identifier: str = self._parse_security_identifier()
        self._country_code: str = self._parse_country()
        self._check_digit: str = self._parse_check_digit()

        isin_length = len(isin)
        if isin_length != 12:
            raise ValueError(f'ISIN codes must always be 12 characters, not {isin_length}')

    def __str__(self):
        return f'ISIN={self._isin}'

    def __repr__(self):
        # automatically get name to minimise refactor touch points
        return f'{self.__class__.__name__}(isin={self._isin})'

    @property
    def country_code(self) -> str:
        return self._country_code

    @property
    def check_digit(self) -> str:
        return self._check_digit

    @property
    def security_identifier(self) -> str:
        return self._security_identifier

    def _parse_country(self) -> str:
        """
        As per the ISIN format documentation listed in the module docstring,
        the 2-letter country code will always be found in the first two chars
        of the ISIN code.

        https://www.isin.org/country-codes/

        Returns:
            str: The 2-letter country code of the ISIN

        """
        country_code: str = self._isin[0:2]
        assert country_code.isalpha()
        return country_code

    def _parse_check_digit(self) -> str:
        """
        The check_digit is used for validation via the Luhn algorithm.
        https://en.wikipedia.org/wiki/Luhn_algorithm

        Returns:
            str: the check_digit
        """
        check_digit: str = self._isin[-1]
        assert check_digit.isnumeric()
        return check_digit

    def _parse_security_identifier(self) -> str:
        security_identifier: str = self._isin[2:11]
        assert security_identifier.isalnum()
        return security_identifier

    # def _compute_check(self) -> str:
    #     """
    #     The check is performed using the Luhn algorithm
    #     https://en.wikipedia.org/wiki/Luhn_algorithm
    #
    #     # TODO: add ability to compute the check, will be available after
    #     Returns:
    #         str
    #     Raises
    #         NotImplementedError
    #     """
    #
    #     for character in list(self._country_code):
    #         value = ord(character)
    #         print(value)
