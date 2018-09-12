class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[True] + [False] * len(s)]
        for i, pc in enumerate(p):
            row = [pc == '*' and dp[-2][0]]
            for j, sc in enumerate(s):
                if pc == '.':
                    row.append(dp[-1][j])
                elif pc == '*':
                    row.append(
                        dp[-2][j + 1] or ((p[i - 1] == '.' or p[i - 1] == sc) and row[j]))
                else:
                    row.append(dp[-1][j] and pc == sc)
            dp.append(row)
        return dp[-1][-1]

        """
        m = len(s)
        n = len(p)
        # Init dp
        dp = [[False for i in range(n + 1)] for i in range(m + 1)]
        # When string and pattern are all None
        dp[m][n] = True
        # When the string is None, pattern like "a*" can still match it
        for i in range(n - 1, -1, -1):
            if p[i] == "*":
                dp[m][i] = dp[m][i + 1]
            elif i + 1 < n and p[i + 1] == "*":
                dp[m][i] = dp[m][i + 1]
            else:
                dp[m][i] = False

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # When the current character is "*"
                if p[j] == "*":
                    if j - 1 >= 0 and p[j - 1] != "*":
                        dp[i][j] = dp[i][j + 1]
                    # If the pattern is starting with "*" or has "**" in it
                    else:
                        return False
                # When the the second character of pattern is "*"
                elif j + 1 < n and p[j + 1] == "*":
                    # When the current character matches, there are three possible situation
                    # 1. ".*" matches nothing
                    # 2. "c*" matches more than one character
                    # 3. "c*" just matches one character
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i][j + 2] or dp[i + 1][j] or dp[i + 1][j + 2]
                    # Ignore the first two characters("c*") in pattern since they cannot match
                    # the current character in string
                    else:
                        dp[i][j] = dp[i][j + 2]
                else:
                    # When the current character is matched
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i + 1][j + 1]
                    else:
                        dp[i][j] = False
        return dp[0][0]
        """
