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