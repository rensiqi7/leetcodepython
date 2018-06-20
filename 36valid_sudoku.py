class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cell = [[] for i in range(9)]
        col = [[] for i in range(9)]
        row = [[] for i in range(9)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '.':
                    k = (i // 3) * 3 + j // 3
                    if num in row[i] + col[j] + cell[k]:
                        return False
                    row[i].append(num)
                    col[j].append(num)
                    cell[k].append(num)

        return True
