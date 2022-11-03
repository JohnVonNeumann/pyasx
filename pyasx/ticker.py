from enum import Enum

from pyasx.exceptions import InvalidTickerLengthException


class Ticker:
    """
    Insert
    """

    def __init__(self, *, ticker: str):
        self._ticker: str = ticker
        self._ticker_length: int = len(ticker)
        self._ticker_type: str = self._process_ticker_type()

    @property
    def ticker(self) -> str:
        return self._ticker

    @ticker.setter
    def ticker(self, value: str):
        ticker_length: int = len(value)
        if not 3 <= ticker_length <= 6:
            raise InvalidTickerLengthException(
                f'Tickers must be minimum 3 and maximum 6 characters, not {ticker_length}'
            )
        else:
            self._ticker = value

    @property
    def ticker_type(self) -> str:
        return self._ticker_type

    def _process_ticker_type(self) -> str:
        # https://www2.asx.com.au/markets/market-resources/asx-codes-and-descriptors
        # https://www2.asx.com.au/content/dam/asx/investors/investment-options/asx-issuer-code-allocation-2017.pdf
        match self._ticker_length:
            case 3:
                return TickerType.ORDINARY_SHARE
            case 4:
                raise NotImplementedError
            case 5:
                raise NotImplementedError
            case 6:
                raise NotImplementedError
            case _:
                raise InvalidTickerLengthException


class TickerType(Enum):
    """
    ETPs include Exchange Traded Funds (ETFs), Managed Funds and Structured
    Products. Most Exchange Traded Funds and Managed Funds have a 3 or 4
    character codes that reflect the name of the fund. N    ew Exchange Traded
    Funds and Managed Funds will all have a 4 character codes that reflect
    the name of the fund.

    Structured Products and Single Asset Funds have 6 character codes, with
    the first three characters reflecting the name of the issuer or fund.

    """

    # https://www2.asx.com.au/content/dam/asx/investors/investment-options/asx-issuer-code-allocation-2017.pdf
    ORDINARY_SHARE: str = "ORDINARY_SHARE"
    EXCHANGE_TRADED_FUND: str = "EXCHANGE_TRADED_FUND"
    MANAGED_FUND: str = "MANAGED_FUND"
    STRUCTURED_PRODUCT: str = "STRUCTURED_PRODUCT"
    WARRANT: str = "WARRANT"
    AUSTRALIAN_GOVERNMENT_BOND: str = "AUSTRALIAN_GOVERNMENT_BOND"
    INTEREST_RATE_SECURITY: str = "INTEREST_RATE_SECURITY"
