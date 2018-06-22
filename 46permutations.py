class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums.sort()
        res = [nums[:]]
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                j = n - 1
                while nums[j] < nums[i - 1]:
                    j -= 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                nums[i:] = sorted(nums[i:])
                res.append(nums[:])
                i = n - 1
            else:
                i -= 1

        return res

# from itertools import *
# class Solution:
#    def permute(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: List[List[int]]
#        """
#        return list(permutations(nums, len(nums)))
