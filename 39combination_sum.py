class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtracing(nums, target, idx, path, ret):
            if not target:
                ret.append(path)
                return
            for i in range(idx, len(nums)):
                if target < nums[i]:
                    break
                backtracing(nums, target - nums[i], i, path + [nums[i]], ret)
        ret = []
        candidates.sort()
        backtracing(candidates, target, 0, [], ret)
        return ret

#     def dfs(self, nums, target, index, path, res):
#         if target < 0:
#             return  # backtracking
#         if target == 0:
#             res.append(path)
#             return
#         for i in range(index, len(nums)):
#             if nums[i] > target :
#                 break
#             self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
