import unittest
from src.part1 import TrebuchetPart1

class TestTrebuchetPart1(unittest.TestCase):

    def test_single_line(self):
        lines = ["1abc2"]
        self.assertEqual(TrebuchetPart1().calculate(lines), 12)

    def test_single_digit(self):
        lines = ["treb7uchet"]
        self.assertEqual(TrebuchetPart1().calculate(lines), 77)

    def test_multiple_digit(self):
        lines = ["a1b2c3d4e5f"]
        self.assertEqual(TrebuchetPart1().calculate(lines), 15)

    def test_no_digits(self):
        lines = ["abcdef"]
        self.assertEqual(TrebuchetPart1().calculate(lines), 0)

    def test_empty_lines(self):
        lines = [""]
        self.assertEqual(TrebuchetPart1().calculate(lines), 0)


if __name__ == '__main__':
    unittest.main()