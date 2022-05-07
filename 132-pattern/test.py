import unittest
from onethreetwo_pattern import Solution
from large_problem import large_problem


class TestSolution(unittest.TestCase):


    def test_1(self):
        s = Solution()
        result = s.find132pattern([3,1,4,2])
        self.assertEqual(result, True)

    def test_2(self):
        s = Solution()
        result = s.find132pattern([1,2,3,4,-4,-3,-5,-1])
        self.assertEqual(result, False)

    def test_3(self):
        s = Solution()
        result = s.find132pattern(large_problem)
        # I do not know what the expected result is
        self.assertEqual(result, False)

    def test_4(self):
        s = Solution()
        result = s.find132pattern([3,5,0,3,4])
        self.assertEqual(result, True)



try:
    unittest.main()
except SystemExit:
    None