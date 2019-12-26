class Solution:
    
    def rob(self, H):
    
        if not H: return 0
        
        dp = [0]*(len(H)+1)
        dp[1] = H[0]
        
        for i in range(1, len(H)):
        
            ind = i + 1
            
            dp[ind] = max(dp[ind-1], dp[ind-2] + H[i])
        
        return dp[-1]

# Or using constant space O(1)

    def rob(self, H):
        
        if not H: return 0
        
        pre, cur = 0, H[0]
        
        for i in range(1, len(H)):
            
            pre, cur = cur, max(cur, pre + H[i])
        
        return cur