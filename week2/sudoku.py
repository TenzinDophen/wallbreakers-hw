class Solution:
    def isValidSudoku(self, board):
     
        row = [["" for _ in range(9)] for _ in range(9)]
        col = [["" for _ in range(9)] for _ in range(9)]
        box = [["" for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if (c == '.'):
                    continue
                c = int(c)
                if (c < 0 or c > 9):
                    return False

                number = c - 1
                if (row[i][number] or col[j][number] or box[(i // 3) * 3 + j // 3][number]):
                    return False

                row[i][number] = True
                col[j][number] = True
                box[(i // 3) * 3 + j // 3][number] = True

        return True



