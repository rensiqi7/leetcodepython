class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        temp = '1'
        for _ in range(n - 1):
            num = ''
            i = 0
            count = 1
            while i < len(temp):
                if i + 1 < len(temp) and temp[i] == temp[i + 1]:
                    count += 1
                    i += 1
                    continue
                num = num + str(count) + temp[i]
                count = 1
                i += 1
            temp = num
        return temp


"""
class Solution:
    def countAndSay(self, n):
        result = "1"
        for __ in range(1, n):
            result = self.getNext(result)
        return result

    def getNext(self, s):
        result = []
        start = 0
        while start < len(s):
            curr = start + 1
            while curr < len(s) and s[start] == s[curr]:
                curr += 1
            result.extend((str(curr - start), s[start]))
            start = curr
        return "".join(result)
"""
