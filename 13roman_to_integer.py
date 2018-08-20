class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        hmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = hmap[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if hmap[s[i]] < hmap[s[i + 1]]:
                ans -= hmap[s[i]]
            else:
                ans += hmap[s[i]]
        return ans
        """
        table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
        returnint=0
        for pair in table:
            continueyes=True
            while continueyes:
                if len(s)>=len(pair[0]):
                    if s[0:len(pair[0])]==pair[0]:
                        returnint+=pair[1]
                        s=s[len(pair[0]):]
                    else: continueyes=False
                else: continueyes=False
        return returnint
        """
