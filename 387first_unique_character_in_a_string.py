class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return -1
        p = len(s)
        alphabet = "zxcvbnmasdfghjklqwertyuiop"
        for i in alphabet:
            start = s.find(i)
            end = s.rfind(i)
            if start != -1 and start == end:
                p = min(p, start)
        if p == len(s):
            return -1
        return p


"""
from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):

        lookup = defaultdict(int)
        candidtates = set()
        for i, c in enumerate(s):
            if lookup[c]:
                candidtates.discard(lookup[c])
            else:
                lookup[c] = i+1
                candidtates.add(i+1)

        return min(candidtates)-1 if candidtates else -1
"""
