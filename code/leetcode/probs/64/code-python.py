// In-place
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
                  
        m, n = len(grid), len(grid[0])

        for i in range(m):
             for j in range(n):
                if i == 0 and j == 0: 
                    continue
                elif i == 0: 
                    grid[i][j] += grid[i][j-1]
                elif j == 0: 
                    grid[i][j] += grid[i-1][j]
                else: 
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]


// 1D
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
                      
        dp = [grid[0][0]]
        
        for c in range(1, len(grid[0])):
            dp.append(grid[0][c] + dp[-1])
        
        for r in range(1, len(grid)):
            for c in range(len(grid[0])):
                if c == 0:
                    dp[c] += grid[r][c]
                else:
                    dp[c] = min(dp[c-1], dp[c]) + grid[r][c]

        return dp[-1]