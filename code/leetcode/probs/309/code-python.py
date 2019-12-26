class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
    
        if not prices: return 0
        
        dp = [0]*len(prices)
        
        low = prices[0]
        
        for i in range(1, len(prices)):
            
            low = min(low, prices[i] - dp[max(0, i-2)])
            
            dp[i] = max(dp[i-1], prices[i] - low)
        
        return dp[-1]