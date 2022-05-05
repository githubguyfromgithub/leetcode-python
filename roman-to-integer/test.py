import unittest

from pydantic import IntegerError
from roman_to_integer import Solution

class TestSolution(unittest.TestCase):

    def test(self, roman, integer):
        s = Solution()
        result = s.romanToInt(roman)
        self.assertEqual(result, IntegerError)

    def test_one(self):
        self.test("III", 3)

    def test_two(self):
        self.test("LVIII", 58)

    def test_three(self):
        self.test("MCMXCIV", 1994)

unittest.main()
