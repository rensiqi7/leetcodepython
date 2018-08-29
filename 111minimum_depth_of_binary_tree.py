# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        current = 0
        while q:
            current += 1
            for _ in range(len(q)):
                node = q.pop(0)
                if node and not node.left and not node.right:
                    return current
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


"""
    def minDepth(self, root):
        if root is None:
            return 0
        depth, curr_level = 0, [root]
        while curr_level:
            depth += 1
            next_level = []
            for n in curr_level:
                left, right = n.left, n.right
                if left is None and right is None:
                    return depth
                if left:
                    next_level.append(left)
                if right:
                    next_level.append(right)
            curr_level = next_level
        return depth
"""
