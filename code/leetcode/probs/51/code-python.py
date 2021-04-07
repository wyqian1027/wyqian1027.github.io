class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["."]*n for _ in range(n)]
        results = []

        def checkV(row, col, board):
            for i in range(row):
                if board[i][col] == "Q": return False
            return True

        def checkX(row, col, board):
            while row-1 >= 0 and col-1 >= 0:
                if board[row-1][col-1] == "Q": return False
                row, col = row-1, col-1
            return True

        def checkX2(row, col, board):
            while row-1 >= 0 and col+1 < n:
                if board[row-1][col+1] == "Q": return False
                row, col = row-1, col+1
            return True

        def dfs(board, row):
            if row >= n:
                results.append(["".join(sub) for sub in board])
                return
            for i in range(n):
                if checkV(row, i, board) and checkX(row, i, board) \
                    and checkX2(row, i, board):
                    board[row][i] = "Q"
                    dfs(board, row+1)
                    board[row][i] = "."
        dfs(board, 0)
        return results
