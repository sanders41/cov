import sys

from cov import main


def test_main():
    assert main.main() == 1


if sys.version_info < (3, 12):

    def test_hi():
        assert main.hi() == "hi"


if sys.version_info > (3, 11):

    def test_bye():
        assert main.bye() == "bye"
