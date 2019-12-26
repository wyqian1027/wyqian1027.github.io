class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if not prices: return 0
        
        if k >= len(prices)//2:
            ans, pre = 0, float('inf')
            for x in prices:
                if x > pre: ans += x - pre
                pre = x
            return ans
        
        dp = [[0]*len(prices) for _ in range(k+1)]
        
        for i in range(1, k+1):
            low = prices[0]
            for j in range(1, len(prices)):
                low = min(low, prices[j] - dp[i-1][j-1])
                dp[i][j] = max(dp[i][j-1], prices[j] - low)
        
        return dp[-1][-1]