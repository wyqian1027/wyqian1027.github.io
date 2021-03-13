class Solution:
    def uniquePathsWithObstacles(self, grid):
        rowN, colN = len(grid), len(grid[0])
        dp = [0]*colN
        dp[0] = 1
        for r in range(rowN):
            for c in range(colN):
                
                if grid[r][c] == 1:
                    dp[c] = 0
                elif 0 <= c-1:
                    dp[c] += dp[c-1]
        return dp[-1]

# 2D
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[m-1][n-1] == 1: return 0
        dp = [[-1]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        def cal(r, c):
            if r >= m or c >= n or grid[r][c] == 1:
                return 0
            if dp[r][c] != -1: 
                return dp[r][c]
            dp[r][c] =  cal(r+1, c) + cal(r, c+1)
            return dp[r][c]
        return cal(0, 0)
