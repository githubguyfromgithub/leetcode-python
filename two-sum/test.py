import unittest
from two_sum import Solution


class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        result = s.twoSum([2,7,11,15], 9)
        self.assertEqual([0,1],result)

    def test_two(self):
        s = Solution()
        result = s.twoSum([3, 2, 4], 6)
        self.assertEqual([1,2],result)

    def test_three(self):
        s = Solution()
        result = s.twoSum([3, 3], 6)
        self.assertEqual([0, 1], result)





unittest.main()