class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        
        acc = [] 
        cur = 0
        n = len(A)
        dp = [[0]*n for _ in range(K)]
        
        # building prefix-sum and initialize dp[0]
        for i, num in enumerate(A):
            cur += num
            acc.append(cur)
            dp[0][i] = cur / (i+1)
            
        max_sum = dp[0][-1]
        
        for i in range(1, K):
            
            for j in range(i, n):
                
                dp[i][j] = max(dp[i-1][k] + (acc[j] - acc[k]) / (j - k) for k in range(i-1, j))
                
            max_sum = max(max_sum, dp[i][-1])
        
        return max_sum