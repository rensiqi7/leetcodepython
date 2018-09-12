class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in xrange(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result


"""
def reverse_bit(num):
    result = 0
    while num:
        result = (result << 1) + (num & 1)
        num >>= 1
    return result
"""

"""
def reverse_int(x):
    result = 0
    pos_x = abs(x)
    while pos_x:
        result = result * 10 + pos_x % 10
        pos_x /= 10
    return result if x >= 0 else (-1) * result
"""
