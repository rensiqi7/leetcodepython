class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] = d[n] + 1

        results = set([])
        if 0 in d and d[0] >= 3:
            results.add((0, 0, 0))

        pns = sorted(filter(lambda x: x >= 0, nums), reverse=True)
        nns = sorted(filter(lambda x: x < 0, nums))

        for pn in pns:
            for nn in nns:
                r = -(pn + nn)
                if r in d:
                    if r in [pn, nn] and d[r] > 1:
                        results.add((nn, r, pn))
                    elif r < nn:
                        results.add((r, nn, pn))
                    elif r > pn:
                        results.add((nn, pn, r))

        return [list(t) for t in results]


"""
class Solution(object):
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return result
"""
