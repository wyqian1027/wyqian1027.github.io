class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        empty = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    empty += 1
                if grid[i][j] == 1:
                    start_r, start_c = i, j
        
        grid[start_r][start_c] = 0
        self.ans = 0
    
        def dfs(r, c, grid, empty):
            
            if 0 <= r < len(grid) and 0<= c < len(grid[0]):
                
                if grid[r][c] == -1:
                    return
                
                if grid[r][c] == 2:
                    if empty == 0:
                        self.ans += 1
                    return

                if grid[r][c] == 0:

                    grid[r][c] = -1

                    dfs(r+1, c, grid, empty-1)
                    dfs(r-1, c, grid, empty-1)
                    dfs(r, c+1, grid, empty-1)
                    dfs(r, c-1, grid, empty-1)
                    
                    grid[r][c] = 0   # backtracking
        
        dfs(start_r, start_c, grid, empty+1)
        
        return self.ans
            
        