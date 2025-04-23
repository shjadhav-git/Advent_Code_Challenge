import unittest
from src.part2 import TrebuchetPart2

class TestTrebuchetPart2(unittest.TestCase):

    def test_word_digit(self):
        lines = ["eightwothree"]
        self.assertEqual(TrebuchetPart2().calculate(lines), 83)

    def test_numeric_digits(self):
        lines = ["4nineeightseven2"]
        self.assertEqual(TrebuchetPart2().calculate(lines), 42)

    def test_no_digits(self):
        lines = ["hello"]
        self.assertEqual(TrebuchetPart2().calculate(lines), 0)

    def test_word_and_numeric(self):
        lines = ["zoneight234"]
        self.assertEqual(TrebuchetPart2().calculate(lines), 14)

    def test_numeric_and_word(self):
        lines = ["1abcseven"]
        self.assertEqual(TrebuchetPart2().calculate(lines), 17)


if __name__ == '__main__':
    unittest.main()