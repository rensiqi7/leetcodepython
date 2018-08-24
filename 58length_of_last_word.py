class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        index = length - 1
        while index >= 0 and s[index] == " ":
            index -= 1
        temp = index
        while index >= 0 and s[index] != " ":
            index -= 1
        return temp - index


"""
        words = s.split()

        if words != []:
            return len(words[-1])

        return 0
"""
