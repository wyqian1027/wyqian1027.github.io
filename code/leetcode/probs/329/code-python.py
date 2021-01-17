# 0. DFS with memorization (2021)
# Probably simpler

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        ans = [[-1]*n for _ in range(m)]
        
        def dfs(i, j, prev):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if matrix[i][j] <= prev: return 0
            if ans[i][j] != -1: return ans[i][j]
            cur = matrix[i][j]
            maxLen = 1 + max(dfs(i+1, j, cur), dfs(i-1, j, cur), \
                             dfs(i, j+1, cur), dfs(i, j-1, cur))
            ans[i][j] = maxLen
            return maxLen
        
        return max(dfs(i, j, float('-inf')) for i in range(m) for j in range(n))

# 1. DFS with memorization

class Solution:
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix: return 0
        self.rowN, self.colN = len(matrix), len(matrix[0])
    
        dic = {}
        ans = 0
        for i in range(self.rowN):
            for j in range(self.colN):
                ans = max(ans, self.dfs(i, j, 1, matrix, dic))
        return ans
    
    def dfs(self, r, c, path, matrix, dic):
        
        if (r, c) in dic: return dic[(r, c)]
        maxPath = 1
        for ir, ic in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + ir, c + ic
            if 0 <= nr < self.rowN and 0 <= nc < self.colN and \
            matrix[nr][nc] > matrix[r][c]:
                maxPath = max(maxPath, path + self.dfs(nr, nc, 1, matrix, dic))
        dic[(r,c)] = maxPath
        return maxPath
        
# 2. "Peeling Onion" Topological Sorting

class Solution:
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix: return 0
        self.rowN, self.colN = len(matrix), len(matrix[0])

        indegree = [[0]*self.colN for _ in range(self.rowN)]
        for i in range(self.rowN):
            for j in range(self.colN):
                for ir, ic in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = i + ir, j + ic                
                    if 0 <= nr < self.rowN and 0 <= nc < self.colN and \
                    matrix[nr][nc] > matrix[i][j]:
                        indegree[i][j] += 1
        
        start = collections.deque()
        for i in range(self.rowN):
            for j in range(self.colN):
                if indegree[i][j] == 0:
                    start.append((i, j))

        layer = 0
        while start:
            size = len(start)
            for _ in range(size):
                r, c = start.popleft()
                for ir, ic in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = r + ir, c + ic
                    if 0 <= nr < self.rowN and 0 <= nc < self.colN and \
                    matrix[nr][nc] < matrix[r][c]:
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            start.append((nr, nc))
            layer += 1
        
        return layer