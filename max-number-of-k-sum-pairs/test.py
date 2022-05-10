import unittest
from max_number_of_k_sum_pairs import Solution


class TestSolution(unittest.TestCase):
    def run_test(self, nums, k, expected):
        s = Solution()
        result = s.maxOperations(nums, k)
        self.assertEqual(result, expected)

    def test_one(self):
        self.run_test([1,2,3,4], 5, 2)

    def test_two(self):
        self.run_test([3,1,3,4,3], 6, 1)

try:
    unittest.main()
except SystemExit:
    None