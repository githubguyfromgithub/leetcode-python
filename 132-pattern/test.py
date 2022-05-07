import unittest
from onethreetwo_pattern import Solution


class TestSolution(unittest.TestCase):


    def test_one(self):
        s = Solution()
        result = s.find132pattern([3,1,4,2])
        self.assertEqual(result, True)

    def test_two(self):
        s = Solution()
        result = s.find132pattern([1,2,3,4,-4,-3,-5,-1])
        self.assertEqual(result, False)


try:
    unittest.main()
except SystemExit:
    None