class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        
        A = list(A)
        B = list(B)
        return self.dfs(A, B, 0, {})
        
    def dfs(self, A, B, loc, cache):
        if A == B:
            return 0
        if tuple(A) in cache:
            return cache[tuple(A)]
        i = loc
        while i < len(A) and A[i] == B[i]:
            i += 1
        min_k = float('inf')
        for j in range(i+1, len(A)):
            if A[j] == B[j]: continue
            if A[j] == B[i]: 
                A[i], A[j] = A[j], A[i]
                min_k = min(min_k, self.dfs(A, B, i+1, cache) + 1)
                A[i], A[j] = A[j], A[i]
        cache[tuple(A)] = min_k
        return min_k