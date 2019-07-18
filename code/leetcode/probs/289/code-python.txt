class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Notations:
        -1: current dead, next gen alive
         0: still dead  (no need update)
         1: still alive (no need update)
         2: current alive, next gen dead
        """
        m, n = len(board), len(board[0])
        DIRS = [[-1, -1], [-1, 0], [-1, 1],\
                [0, -1], [0, 1], \
                [1, -1], [1, 0], [1, 1]]
        
        def check(r, c):
            count = 0
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] > 0:
                    count += 1
            if board[r][c] == 1 and (count < 2 or count > 3):
                board[r][c] = 2
            elif board[r][c] == 0 and count == 3:
                board[r][c] = -1
        
        for r in range(m):
            for c in range(n):
                check(r, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == -1:
                    board[r][c] = 1
                elif board[r][c] == 2:
                    board[r][c] = 0