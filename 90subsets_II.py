class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        l_nums = len(nums)
        visited = [0 for _ in range(l_nums)]
        result = []
        self.dfs(nums, [], 0, visited, result)
        return result

    def dfs(self, nums, curr, idx, visited, result):
        l_nums = len(nums)
        result.append(list(curr))

        for i in range(idx, l_nums):
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
                continue
            curr.append(nums[i])
            visited[i] = 1
            self.dfs(nums, curr, i + 1, visited, result)
            curr.pop()
            visited[i] = 0

    """
    nums.sort()
    def backtrack(start, temp):
        res.append(temp[:])
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            backtrack(i + 1, temp)
            temp.pop()

    res = []
    backtrack(0, [])
    return res
    """
    """
    nums.sort()
        result = [[]]
        previous_size = 0
        for i in xrange(len(nums)):
            size = len(result)
            for j in xrange(size):
                # Only union non-duplicate element or new union set.
                if i == 0 or nums[i] != nums[i - 1] or j >= previous_size:
                    result.append(list(result[j]))
                    result[-1].append(nums[i])
            previous_size = size
        return result
    """
