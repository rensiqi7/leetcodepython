class Solution:

    dictionary = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = 0
        if n == 0 or n == 1:
            return 1
        if n in self.dictionary:
            return self.dictionary[n]
        else:
            number += self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.dictionary[n] = number
        return number


'''
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        dp = [0 for __ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
'''
