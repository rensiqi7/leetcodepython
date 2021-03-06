class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(offset, prefix):
            if len(prefix) == k:
                res.append(prefix)
                return
            remaining = k - len(prefix)
            i = offset
            while i <= n and remaining <= n - i + 1:
                helper(i + 1, prefix + [i])
                i += 1
        res = []
        helper(1, [])
        return res


"""
class Solution(object):
    def combine(self, n, k):
        if k == 1:
            return [[i + 1] for i in range(n)]
        result = []
        if n > k:
            result = [r + [n] for r in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)
        else:
            result = [r + [n] for r in self.combine(n - 1, k - 1)]
        return result
"""
