from functools import lru_cache

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        DIRS = [[-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, -2], [1, 2], [2, -1], [2, 1]]
              
        # cache = {}
        
        @lru_cache(None)
        def calculate(N, K, r, c):

            # p = tuple([N, K, r, c])
            # if p in cache: return cache[p]
            ans = 0
            if K == 0:
                ans = 0 <= r < N and 0 <= c < N
            else:
                for dr, dc in DIRS:
                    if 0 <= r + dr < N and 0 <= c + dc < N:
                        ans += calculate(N, K-1, r+dr, c+dc) / 8
            # cache[p] = ans
            return ans

        return calculate(N, K, r, c)