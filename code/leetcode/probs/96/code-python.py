class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in range(1, n+1):
            for k in range(0, i):
                
                dp[i] += dp[k]*dp[i-1-k] 
            
        return dp[-1]