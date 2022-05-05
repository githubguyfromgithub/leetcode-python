import unittest

from pydantic import IntegerError
from roman_to_integer import Solution

class TestSolution(unittest.TestCase):

    def run_test(self, roman, integer):
        s = Solution()
        result = s.romanToInt(roman)
        self.assertEqual(result, IntegerError)

    def test_one(self):
        self.run_test("III", 3)

    def test_two(self):
        self.run_test("LVIII", 58)

    def test_three(self):
        self.run_test("MCMXCIV", 1994)

unittest.main()
