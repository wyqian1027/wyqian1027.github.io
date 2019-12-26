# Straightforward Python BFS approach. Not the best.

from collections import deque
class Solution:
    def cutOffTree(self, A: List[List[int]]) -> int:
        
        m, n = len(A), len(A[0])
        d = {}
        for i in range(m):
            for j in range(n):
                if A[i][j] > 1:
                    d[A[i][j]] = (i, j)
        
        order = sorted(d.keys())
        
        def get_step(r1, c1, r2, c2):
            q = deque()
            q.append((r1, c1, 0))
            visited = set()
            visited.add((r1, c1))
            while q:
                r, c, step = q.popleft()
                if r == r2 and c == c2:
                    return step
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= nr < m and 0 <= nc < n and A[nr][nc] != 0 and (nr, nc) not in visited:
                        q.append((nr, nc, step+1))
                        visited.add((nr, nc))
                    if nr == r2 and nc == c2:
                        return step + 1
            return -1
        
        total = 0
        r1, c1 = 0, 0
        for el in order:
            r2, c2 = d[el]
            s = get_step(r1, c1, r2, c2)
            # print("from ", r1, c1, " to ", r2, c2, ": ", s)
            if s == -1: return -1
            total += s
            r1, c1 = r2, c2
        
        return total