class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        cache = {}
        
        def compute(i, j):
            if i == j: return 1
            if i > j: return 0
            
            if i < 0: i = 0
            if j >= n: j = n- 1
            
            if (i,j) not in cache:
                if s[i] == s[j]:
                    cache[(i,j)] = compute(i+1, j-1) + 2
                else:
                    cache[(i,j)] = max(compute(i+1, j), compute(i, j-1))
                
            return cache[(i, j)]
        
        return compute(0, n-1)