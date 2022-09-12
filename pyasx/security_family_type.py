"""
Contains an Enum that represents the different types of Securities that
can be available.
"""

from enum import Enum


class SecurityFamilyType(Enum):
    """
    Enum Type that allows users to select a type of Security.
    """
    DEBT = 'debt'
    EQUITY = 'equity'
    DERIVATIVE = 'derivative'
    HYBRID = 'hybrid'
