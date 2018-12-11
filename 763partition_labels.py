class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        r = sorted([S.find(s), S.rfind(s)] for s in set(S))
        ans = []
        for dist in r:
            front, rear = dist
            if len(ans) == 0:
                ans.append(dist)
            else:
                if front > ans[-1][-1]:
                    ans.append(dist)
                else:
                    ans[-1][-1] = max(ans[-1][-1], rear)
        return [rear - front + 1 for [front, rear] in ans]

        """
        if not S:
            return []
        last_index = {c : i for i, c in enumerate(S)}
        rst = []
        l, r = 0, 0
        for i, c in enumerate(S):
            r = max(r, last_index[c])
            if i == r:
                rst.append(r - l + 1)
                l = i + 1
        return rst
        """
