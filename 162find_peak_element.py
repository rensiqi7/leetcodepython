class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) / 2 + l
            left = nums[mid - 1] if mid > 0 else float('-inf')
            right = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')
            if nums[mid] > left and nums[mid] > right:
                return mid
            elif nums[mid] < left:
                r = mid - 1
            else:
                l = mid + 1
        return -1
