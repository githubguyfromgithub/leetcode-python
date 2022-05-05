import unittest
from longest_common_prefix import Solution


class TestSolution(unittest.TestCase):

    def test(self, input, expected):
        s = Solution()
        result = s.longestCommonPrefix(input)
        self.assertEqual(result, expected)

    def test_one(self):
        self.test(["flower","flow","flight"], "fl")

    def test_two(self):
        self.test(["dog","racecar","car"], "")


unittest.main()