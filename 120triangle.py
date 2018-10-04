class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        result = [0 for i in range(len(triangle))]
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        result[0] = triangle[0][0]
        for i in range(1, len(triangle)):

            curarr = triangle[i]
            result[i] = result[i - 1] + curarr[i]
            for j in range(1, i)[::-1]:
                result[j] = min(result[j - 1], result[j]) + curarr[j]
            result[0] = result[0] + curarr[0]

        max_result = result[0]
        for i in range(len(result)):
            max_result = min(max_result, result[i])
        return max_result
