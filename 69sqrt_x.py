class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 1.0
        while abs(result * result - x) > 0.1:
            result = (result + x / result) / 2
        return int(result)
# Newton's method
