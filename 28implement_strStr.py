class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack or not needle:
            return 0
        length = len(needle)
        for i in range(len(haystack) - length + 1):
            if haystack[i:i + length] == needle:
                return i
        return -1

        """
        str1 = "this is string example....wow!!!";
        str2 = "is";
        print str1.rindex(str2)
        5
        print str1.index(str2)
        2
        """
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        i = 0
        needleLength = len(needle)
        while i < len(haystack):
            a = haystack[i:i + needleLength]
            if haystack[i:i + needleLength] == needle:
                return i
            else:
                index = 0
                try:
                    index = needle.rindex(haystack[i + needleLength])
                except Exception:
                    i += needleLength + 1
                i += needleLength - index
        return -1
        """
        """
        return haystack.find(needle)
        """
