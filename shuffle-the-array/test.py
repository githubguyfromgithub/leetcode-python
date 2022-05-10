import unittest
from shuffle_the_array import Solution


class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        result = s.shuffle([2,5,1,3,4,7], 3)
        self.assertEqual([2,3,5,4,1,7],result)

    def test_two(self):
        s = Solution()
        result = s.shuffle([1,2,3,4,4,3,2,1], 4)
        self.assertEqual([1,4,2,3,3,2,4,1], result)

    def test_three(self):
        s = Solution()
        result = s.shuffle([1,1,2,2], 2)
        self.assertEqual([1,2,1,2], result)

try:
    unittest.main()
except SystemExit:
    None