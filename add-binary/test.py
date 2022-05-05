import unittest
from add_binary import Solution


class TestSolution(unittest.TestCase):
    def run_test(self, a, b, expected):
        s = Solution()
        result = s.addBinary(a, b)
        self.assertEqual(result, expected)

    def test_one(self):
        self.run_test("11", "1", "100")

    def test_two(self):
        self.run_test("1010", "1011", "10101")

try:
    unittest.main()
except SystemExit:
    print('The test exited with a SystemExit')