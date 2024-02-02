import sys


def main() -> int:
    return 1


if sys.version_info < (3, 12):

    def hi() -> str:
        return "hi"


if sys.version_info > (3, 11):

    def bye() -> str:
        return "bye"
