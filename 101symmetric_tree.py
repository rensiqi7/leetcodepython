# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def dfs(left, right):
            if not left and not right:
                return True
            elif left and not right:
                return False
            elif not left and right:
                return False
            elif left.val != right.val:
                return False
            else:
                return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)


"""
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSameTree(root.left, root.right)

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        out_is_same = self.isSameTree(p.right, q.left)
        inside_is_same = self.isSameTree(p.left, q.right)
        root_is_same = p.val == q.val
        return root_is_same and out_is_same and inside_is_same
"""
