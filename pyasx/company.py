"""
The company.py module contains the Company class, used to model a business entity
that is listed on the ASX.
"""

from datetime import datetime

from .ticker import Ticker
from pyasx.exceptions import InvalidTickerLengthException


class Company:
    """
    A company is a business entity that represents the primary asset and concept of the ASX. It is
    a profit making, registered organisation that operates as a business.

    Structure of the data returned so far:
        'ticker': ticker,
        'name': name,
        'listing_date': listing_date,
        'gics_industry': gics,
        'market_cap': market_cap

    """

    def __init__(self, *, ticker: Ticker, name: str):
        self._ticker: Ticker = ticker
        self._name: str = name

    @property
    def ticker(self) -> str:
        return self._ticker.ticker

    @property
    def name(self) -> str:
        return self._name
