# probably better to go from end to front.
from functools import *

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        @lru_cache(None)
        def check(i, j):
            if i > j: return False
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        
        @lru_cache(None)
        def dfs(pos):
            res = []
            for j in range(pos, len(s)):
                if check(pos, j):
                    if j == len(s) - 1: res.append([s[pos:j+1]])
                    for right in dfs(j+1):
                        res.append([s[pos:j+1]] + right)
            return res
                        
        return dfs(0)