class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        per = set()
        for i in nums:
            if not per:
                per.add(tuple([i]))
                continue
            temp = []
            for j in per:
                jl = list(j)
                for k in xrange(len(jl) + 1):
                    temp.append(jl[k:] + [i] + jl[:k])
            per = set()
            for j in temp:
                per.add(tuple(j))

        return [list(i) for i in per]
