class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]: return 0
        maxArea = 0
        m, n = len(grid), len(grid[0])
        
        def getArea(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = -1
                return 1 + getArea(r+1, c) + getArea(r-1, c) +\
                         + getArea(r, c+1) + getArea(r, c-1)
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, getArea(i, j))
        
        return maxArea
