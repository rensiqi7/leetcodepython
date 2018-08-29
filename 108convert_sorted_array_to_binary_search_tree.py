# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums):
            if not nums:
                return None
            start = 0
            end = len(nums) - 1
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = helper(nums[:mid])
            node.right = helper(nums[mid + 1:])
            return node
        return helper(nums)


"""
    def sortedArrayToBST(self, nums):
        return self._sortedArrayToBST(nums, 0, len(nums))

    def _sortedArrayToBST(self, nums, left, right):
        if left == right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self._sortedArrayToBST(nums, left, mid)
        root.right = self._sortedArrayToBST(nums, mid + 1, right)
        return root
""""
