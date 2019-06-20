class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or len(grid) == 0 or len(grid[0]) == 0: return 0
        
        rowN, colN = len(grid), len(grid[0])
        island = 0
        
        for i in range(rowN):
            for j in range(colN):
                if grid[i][j] == '1':
                    island += 1
                    q = collections.deque([(i, j)])
                    grid[i][j] = '0'
                    while q:
                        r, c = q.popleft()
                        for ir, ic in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            nr, nc = r+ir, c+ic
                            if 0 <= nr < rowN and 0 <= nc < colN and grid[nr][nc] == '1':
                                q.append((nr, nc))
                                grid[nr][nc] = '0'
        return island