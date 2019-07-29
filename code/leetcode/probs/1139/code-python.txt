# O(N^3) solution building hor, ver matrix
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        h = [[0]*n for _ in range(m)]
        v = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    h[i][j] = 1 if j == 0 else h[i][j-1] + 1
                    v[i][j] = 1 if i == 0 else v[i-1][j] + 1
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    s = min(h[i][j], v[i][j])
                    while s > count:
                        if v[i][j-s+1] >= s and h[i-s+1][j] >= s:
                            count = max(count, s)
                            break
                        s -= 1
        return count*count
        
# O(N^4) Bruteforce
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        def checkOnes(r1, c1, r2, c2):
            for i in range(c1, c2+1):
                if grid[r1][i] == 0: return False
            for i in range(c1, c2+1):
                if grid[r2][i] == 0: return False
            for j in range(r1, r2+1):
                if grid[j][c1] == 0: return False
            for j in range(r1, r2+1):
                if grid[j][c2] == 0: return False   
            return True
        
        count = 0
        rowN, colN = len(grid), len(grid[0])
        for r2 in range(rowN-1, -1, -1):
            for c2 in range(colN-1, -1, -1):
                shift = min(r2, c2)
                for r1 in range(r2 - shift, r2+1):
                    if count >= (r2 - r1 + 1)**2: break
                    c1 = c2 - (r2 - r1)                         
                    if checkOnes(r1, c1, r2, c2):
                        # print(r1, c1, r2, c2)
                        count = max(count, (r2 - r1 + 1)**2)
                        break
        return count