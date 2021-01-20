class UF:
    def __init__(self, num):   
        self.p = list(range(num))  
        self.rank = [0] * num

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x]) 
        return self.p[x]
        
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:  
            xr, yr = yr, xr
        self.p[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
        return True

    
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:        
        N = m*n
        if N == 0: return [0]*len(positions)
        uf = UF(N)
        grid = [0]*N
        island = 0
        result = []
        for r, c in positions:
            p1 = r*n + c
            if grid[p1] == 0: 
                island += 1
                grid[p1] = 1
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r + dr, c + dc
                    p2 = nr*n+nc
                    if 0 <= nr < m and 0 <= nc < n and grid[p2] == 1:
                        if uf.union(p1, p2):
                            island -= 1
            result.append(island)
        return result
            
            
        
        
