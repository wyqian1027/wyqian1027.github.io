class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        
        if not A or not B: return 0
        
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]: 
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]