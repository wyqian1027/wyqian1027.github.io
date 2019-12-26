class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:
        
        if not A or len(A) == 0 or len(A[0]) == 0: return 0
        
        m, n = len(A), len(A[0])
        dp = [[0]*n for _ in range(m)]
        maximal = 0
        
        for i in range(m):
            for j in range(n):
                # compute
                dp[i][j] = 1 if A[i][j] == '1' else 0
                if dp[i][j] == 1 and i !=0 and j != 0:
                    k = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    dp[i][j] += k
                # update                
                maximal = max(dp[i][j], maximal)

        return maximal**2