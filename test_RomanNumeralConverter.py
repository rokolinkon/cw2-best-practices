from unittest import TestCase, main
from clean_code import RomanNumeralConverter


class TestRomanNumeralConverter(TestCase):
    def setUp(self):
        self.converter = RomanNumeralConverter()

    def tearDown(self):
        del self.converter


if __name__ == '__main__': main()
