class Ticker:

    def __init__(self, *, ticker: str):
        self._ticker: str = ticker
        self._ticker_type: str = self._process_ticker_type()
        # TODO: just use the __len__ dunder method
        self._ticker_length: int = len(ticker)

    @property
    def ticker(self) -> str:
        return self._ticker

    @property
    def ticker_type(self) -> str:
        return self._ticker_type

    def _process_ticker_type(self) -> str:
        match self._ticker_length:
            case 3:
                ...
            case (4 | 5 | 6):
                ...
            case _:
                ...
        ticker_type: str = ""
        raise NotImplementedException