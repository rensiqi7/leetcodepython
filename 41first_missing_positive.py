class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not nums:
            return 1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            if abs(nums[i]) <= n:
                idx = abs(nums[i]) - 1
                nums[idx] = -abs(nums[idx])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
