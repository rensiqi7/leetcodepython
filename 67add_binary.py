class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = int(a, 2) + int(b, 2)
        c = str(bin(c))
        return c[2:]


'''
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = val = 0
        if len(a) < len(b):
            a, b = b, a
        lengthA = len(a)
        lengthB = len(b)
        for i in range(lengthA):
            val = carry
            val += int(a[-(i + 1)])
            if i < lengthB:
                val += int(b[-(i + 1)])
            carry, val = val // 2, val % 2
            result.append(str(val))
        if carry:
            result.append(str(carry))
        return "".join(result[::-1])
'''
