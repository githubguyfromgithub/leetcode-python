import unittest
from balanced_binary_tree import Solution


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestSolution(unittest.TestCase):


    def test_one(self):
        root = TreeNode(
            1,
            None,
            TreeNode(
                2,
                None,
                TreeNode(3)
            )
        )
        s = Solution()
        result = s.isBalanced(root)
        self.assertEqual(result, False)

    def test_two(self):
        root = TreeNode(
            3,
            TreeNode(
                9
            ),
            TreeNode(
                20,
                TreeNode(15),
                TreeNode(7)
            )
        )
        s = Solution()
        result = s.isBalanced(root)
        self.assertEqual(result, True)

try:
    unittest.main()
except SystemExit:
    None