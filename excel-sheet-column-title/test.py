import unittest
from excel_sheet_column_title import Solution


class TestSolution(unittest.TestCase):
    def run_test(self, input, expected):
        s = Solution()
        result = s.convertToTitle(input)
        self.assertEqual(result, expected)

    def test_one(self):
        self.run_test(1, "A")

    def test_two(self):
        self.run_test(28, "AB")

    def test_three(self):
        self.run_test(701, "ZY")


try:
    unittest.main()
except SystemExit:
    None