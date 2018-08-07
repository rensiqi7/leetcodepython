class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[right] == nums[mid]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:  # 升序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 旋转（左大右小）
                if nums[left] > target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
