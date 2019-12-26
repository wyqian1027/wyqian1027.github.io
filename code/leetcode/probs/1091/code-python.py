class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()
        if grid[0][0] == 1 or grid[-1][-1] == 1 : return -1
        q.append((0, 0, 1)) # row, col, depth
        n = len(grid)
               
        grid[0][0] = -1
        while q:
            r, c, depth = q.popleft()
            if (r == n-1 and c == n-1): return depth
            
            # 8 direction
            for ir, ic in [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]:
                nr, nc = r + ir, c + ic
                if (0 <= nr <= n-1) and (0 <= nc <= n-1) and grid[nr][nc] == 0:
                    q.append((nr, nc, depth+1))
                    grid[nr][nc] = -1
        return -1