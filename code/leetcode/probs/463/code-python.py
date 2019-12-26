# Simple O(M*N) Solution
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        total = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 4
                    if i+1 < m and grid[i+1][j] == 1:
                        total -= 2
                    if j+1 < n and grid[i][j+1] == 1:
                        total -= 2
        return total
        