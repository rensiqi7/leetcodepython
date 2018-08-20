class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = str(x)[::-1]
        if(rev == str(x)):
            return True
        else:
            return False

        """
        if x == None or x<0:
            return False
        x = str(x)
        h = 0
        t = len(x)-1
        while h < t:
            if x[h] != x[t]:
                return False
            h += 1
            t -= 1
        return True
        """
