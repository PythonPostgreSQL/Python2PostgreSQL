import os
import sys

def select(what, _from) -> str:
    return "SELECT {what} {_from}".format(what, _from)

if __name__ == "__main__":
    work()
