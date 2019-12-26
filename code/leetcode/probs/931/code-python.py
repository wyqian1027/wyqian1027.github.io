# Bottom-Up
class Solution:
    
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        
        dp = [[0]*len(A[0]) for _ in range(len(A))]
        for i in range(len(A[0])):
            dp[0][i] += A[0][i]
        
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                dp[i][j] = min(dp[i-1][j], dp[i-1][min(j+1, len(A[0])-1)], dp[i-1][max(j-1,0)]) + A[i][j]
        
        return min(dp[-1])

# Top-Down
class Solution:
    
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        
        cache = {}
        
        def dp(r, c):
            
            if (r,c) in cache: return cache[(r,c)]
            
            if r == len(A[0]) - 1:
                return A[r][c]
            
            res = A[r][c] + min(dp(r+1, c), dp(r+1, min(c+1, len(A[0])-1)), dp(r+1, max(c-1, 0)))
            cache[(r,c)] = res 
            return res
        
        return min(dp(0, i) for i in range(len(A[0])))