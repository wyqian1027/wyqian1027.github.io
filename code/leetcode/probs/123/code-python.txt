# DP
class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices: return 0
        
        k = 3
        dp = [[0] * len(prices) for _ in range(k)]
        
        for i in range(1, k):
            low = prices[0]
            for j in range(1, len(prices)):
                low = min(low, prices[j] - dp[i-1][j-1])
                dp[i][j] = max(dp[i][j-1], prices[j] - low)
        
        return dp[-1][-1]

# With Greedy Algorithms, use four variables, O(1) space is used!
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit1 = 0
        maxProfit2 = 0
        low1 = float('inf')
        low2 = float('inf')
        for price in prices:
            maxProfit1 = max(maxProfit1, price - low1)
            low1 = min(low1, price)
            maxProfit2 = max(maxProfit2, price - low2)
            low2 = min(low2, price - maxProfit1)

        return maxProfit2