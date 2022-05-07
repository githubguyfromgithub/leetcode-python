import unittest
from concatenation_of_array import Solution


class TestSolution(unittest.TestCase):
    def run_test(self, input, expected):
        s = Solution()
        result = s.getConcatenation(input)
        self.assertEqual(result, expected)

    def test_one(self):
        self.run_test([1,2,1], [1,2,1,1,2,1])

    def test_two(self):
        self.run_test([1,3,2,1], [1,3,2,1,1,3,2,1])


try:
    unittest.main()
except SystemExit:
    None