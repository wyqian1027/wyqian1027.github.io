class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        
        pre, ans = float('inf'), 0
        
        for x in prices:
            if x > pre:
                ans += x - pre
            pre = x
        
        return ans