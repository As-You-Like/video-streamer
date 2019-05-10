from enum import Enum


def handle(error):
    if error == Error.UNKNOWN_RESPONSE:
        pass


class Error(Enum):
    UNKNOWN_RESPONSE = 1
