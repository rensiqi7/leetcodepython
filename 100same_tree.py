# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        elif not q or not p:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


'''
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # insight: use recursive solution
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        left_is_same = self.isSameTree(p.left, q.left)
        right_is_same = self.isSameTree(p.right, q.right)
        root_is_same = p.val == q.val

        return root_is_same and left_is_same and right_is_same
'''
