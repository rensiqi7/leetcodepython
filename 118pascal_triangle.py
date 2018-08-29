class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        else:
            ans = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(i - 1):
                row.append(ans[i - 1][j] + ans[i - 1][j + 1])
            row.append(1)
            ans.append(row)
        return ans

        """
        if not numRows:
            return []
        result = [[1]]
        while numRows > 1:
            result.append(
                [1] + [a + b for a, b in zip(result[-1][:-1], result[-1][1:])] + [1])
            numRows -= 1
        return result
        """
