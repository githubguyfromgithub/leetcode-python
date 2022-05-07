# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def heightAndIsBalanced(self, root):
        if not(root):
            return True, 0
        isBalanced, leftHeight = self.heightAndIsBalanced(root.left)
        if not isBalanced:
            return False, None
        isBalanced, rightHeight = self.heightAndIsBalanced(root.right)
        if not isBalanced:
            return False, None
        if abs(leftHeight - rightHeight) > 1:
            return False, None
        return True, max(leftHeight, rightHeight) + 1
        
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.heightAndIsBalanced(root)[0]