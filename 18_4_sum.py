class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rt = []
        nums.sort()
        self.nSum(nums, target, 4, [], rt)
        return rt

    def nSum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return
        if target < nums[0] * N or target > nums[-1] * N:
            return

        if N == 2:
            p1 = 0
            p2 = len(nums) - 1
            while p2 > p1:
                if nums[p1] + nums[p2] == target:
                    results.append(result + [nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p2 > p1 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    while p2 > p1 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
                elif nums[p1] + nums[p2] < target:
                    p1 += 1
                else:
                    p2 -= 1

        else:
            for i in range(len(nums) - N + 1):
                if i == 0 or nums[i] != nums[i - 1]:
                    self.nSum(nums[i + 1:], target - nums[i],
                              N - 1, result + [nums[i]], results)
