class Solution:
    """
    Bit Manipulation

    T: O(n)
    S: O(1)

    REF: https://leetcode.com/problems/single-number-ii/discuss/43332
    """

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0

        for num in nums:
            a = (a ^ num) & ~b
            b = (b ^ num) & ~a

        return a

    """
    return int((3*sum(set(nums)) - sum(nums))/2)
    """
