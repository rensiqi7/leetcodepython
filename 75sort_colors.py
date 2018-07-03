class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        s, e, m = 0, 0, len(nums) - 1

        while e <= m:
            if nums[e] < pivot:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e += 1
            elif nums[e] == pivot:
                e += 1
            else:
                nums[m], nums[e] = nums[e], nums[m]
                m -= 1
