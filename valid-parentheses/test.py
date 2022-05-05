import unittest
from valid_parentheses import Solution

class TestSolution(unittest.TestCase):
    def run_test(self, input, expectedResult):
        s = Solution()
        result = s.isValid(input)
        self.assertEqual(result, expectedResult)
    
    def test_one(self):
        self.run_test('()', True)

    def test_two(self):
        self.run_test('()[]{}', True)

    def test_three(self):
        self.run_test('(]', False)



try:
    unittest.main()
except SystemExit:
    print('The test exited with a SystemExit')