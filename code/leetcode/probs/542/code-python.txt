# 1.
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        out = [[float('inf')]*n for _ in range(m)]
        
        # from top left
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    out[i][j] = 0
                else:
                    if i > 0: out[i][j] = min(out[i][j], out[i-1][j] + 1)
                    if j > 0: out[i][j] = min(out[i][j], out[i][j-1] + 1)
        
        # from bottom right
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 1:
                    if i < m-1: out[i][j] = min(out[i][j], out[i+1][j] + 1)
                    if j < n-1: out[i][j] = min(out[i][j], out[i][j+1] + 1)        
        
        return out

# 2.
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        q = collections.deque()
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append([i, j])
                    visited.add((i,j))
        
        out = [[0]*n for _ in range(m)]
        dist = 0
        
        while q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                out[r][c] = dist
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        q.append([nr, nc])
                        visited.add((nr, nc))
            dist += 1
        return out

