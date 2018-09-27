class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        return nums[len(nums) / 2]

        """
        majority_index = 0
        count = 1

        for i in range(1, len(nums)):
            if nums[majority_index] == nums[i]:
                count += 1
            else:
                count -= 1

            if count == 0:
                majority_index = i
                count = 1

        return nums[majority_index]
        """
