import unittest
from longest_common_prefix import Solution


class TestSolution(unittest.TestCase):
    def run_test(self, input, expected):
        s = Solution()
        result = s.longestCommonPrefix(input)
        self.assertEqual(result, expected)

    def test_one(self):
        self.run_test(["flower","flow","flight"], "fl")

    def test_two(self):
        self.run_test(["dog","racecar","car"], "")


unittest.main()