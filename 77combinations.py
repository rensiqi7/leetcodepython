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
