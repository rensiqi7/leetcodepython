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
