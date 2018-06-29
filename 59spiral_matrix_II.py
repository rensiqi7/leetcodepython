class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        left = top = 0
        right = n - 1
        bottom = n - 1
        num = 1
        result = [[0 for __ in range(n)] for __ in range(n)]
        while left < right and top < bottom:
            for i in range(left, right):
                result[top][i] = num
                num += 1
            for i in range(top, bottom):
                result[i][right] = num
                num += 1
            for i in range(right, left, -1):
                result[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                result[i][left] = num
                num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if left == right and top == bottom:
            result[top][left] = num
        return result
