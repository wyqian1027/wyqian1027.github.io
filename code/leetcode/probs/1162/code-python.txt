class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        layer = []
        visited = set()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    layer.append((i, j))
                    visited.add((i, j))
                    
        if len(layer) == n*n or len(layer) == 0: 
            return -1
        
        max_dist = 0
        while layer:
            max_dist += 1
            new_layer = []
            size = len(layer)
            for _ in range(size):
                r, c = layer.pop()
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                        new_layer.append((nr, nc))
                        visited.add((nr, nc))
            layer = new_layer
        
        return max_dist - 1