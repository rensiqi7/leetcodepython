class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ls = list(str(x))
        ch = ls.pop(0)
        if ch == "+" or ch == "-":
            ls.append(ch)
        else:
            ls.insert(0, ch)
        ls.reverse()
        result = int("".join(ls))
        if result > 2147483647 or result < -2147483648:
            result = 0
        return result
