class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        else:
            res = 0
            count = 0
            for i in range(len(nums)):
                count += nums[i]
                if count < 0:
                    count = 0
                else:
                    res = max(res, count)
            if res == 0:
                return max(nums)
            return res


"""
        if not nums:
            return 0
        length = len(nums)
        current = nums[0]
        m = current
        for i in range(1, length):
            if current < 0:
                current = 0
            current += nums[i]
            m = max(current, m)
        return m
"""
