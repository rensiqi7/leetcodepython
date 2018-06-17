class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i < 0:
            nums.reverse()
            return
        j = len(nums) - 1
        while i <= j:
            if nums[i] < nums[j]:
                break
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = sorted(nums[i + 1:])
