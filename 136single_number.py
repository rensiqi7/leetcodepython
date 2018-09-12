class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for val in nums:
            res ^= val
        return res


"""
import operator
from functools import reduce


class Solution:
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)
"""
