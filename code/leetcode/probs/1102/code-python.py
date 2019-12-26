from heapq import *

class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
        m, n = len(A), len(A[0])
        visited = [False]*n*m
        visited[0] = True
        parents = {(0, 0): None}
        
        h = [[-A[0][0], 0, 0]]  # mimicing max-heap 

        # def print_path():
        #     r, c = m - 1, n - 1
        #     while parents[(r, c)]:
        #         print((r, c))
        #         r, c = parents[(r, c)]
        #     print((0, 0))
                
        while h:
            
            score, r, c = heappop(h)
            
            if r == m - 1 and c == n - 1:
                # print_path()
                return -score
            
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and not visited[nr*n + nc]:
                    heappush(h, [-min(-score, A[nr][nc]), nr, nc])
                    # parents[(nr, nc)] = (r, c)
                    visited[nr*n + nc] = True
        return -1