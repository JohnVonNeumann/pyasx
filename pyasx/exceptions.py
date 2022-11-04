class InvalidTickerLengthException(Exception):
    """
    Exception raised when a ticker is not the correct length.

    Correct in this case means minimum 3 and maximum 6 alphanum chars.
    """
    pass
