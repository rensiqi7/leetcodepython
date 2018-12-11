class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lower = 'zxcvbnmasdfghjklqwertyuiop'
        for c in lower:
            if s.count(c) != t.count(c):
                return False
        return True

        """
        if len(s) != len(t):
            return False
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return False
        return True
        """
