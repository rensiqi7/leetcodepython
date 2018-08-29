# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, curr_depth):
            if node is None:
                return True, curr_depth - 1

            left_valid, left_max_depth = helper(node.left, curr_depth + 1)
            if not left_valid:
                return False, None

            right_valid, right_max_depth = helper(node.right, curr_depth + 1)
            if not right_valid:
                return False, None

            if abs(left_max_depth - right_max_depth) > 1:
                return False, None

            return True, max(left_max_depth, right_max_depth)

        return helper(root, 0)[0]


"""
    def isBalanced(self, root):

        return self._isBalanced(root) >= 0

    def _isBalanced(self, root):
        if not root:
            return 0
        left, right = self._isBalanced(root.left), self._isBalanced(root.right)
        if left >= 0 and right >= 0 and abs(left - right) <= 1:
            return 1 + max(left, right)
        else:
            return -1
"""
