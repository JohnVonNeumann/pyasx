from .isin import ISIN

class Security:

    def __init__(self, *,  security_type: str, isin: ISIN, ticker: str, company_name: str):
        self._security_type: str = security_type
        self._isin: ISIN = isin
        self._ticker: str = ticker
        self._company_name: str = company_name

        ticker_length = len(ticker)
        if not 3 <= ticker_length <= 6:
            raise ValueError(f'Ticker codes must be minimum 3 and maximum 6 characters, not {ticker_length}')

    @property
    def security_type(self) -> str:
        return self._security_type

    @property
    def isin(self) -> str:
        return str(self._isin)
    
    @property
    def ticker(self) -> str:
        return self._ticker

    @property
    def company_name(self) -> str:
        return self._company_name

