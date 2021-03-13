from abc import ABC


class KeywordException(Exception, ABC):
    """Exception raised by a keyword from the user"""


class Cancel(KeywordException):
    """User wants to cancel"""


class Quit(KeywordException):
    """User wants to quit"""


ExceptionsKeywordsDict = {
    "quit": Quit,
    "cancel": Cancel,
}


def assert_not_exception_keyword(value: str):
    """Raise KeywordException if value is an exception keyword"""

    if value in ExceptionsKeywordsDict:
        raise ExceptionsKeywordsDict[value]()
