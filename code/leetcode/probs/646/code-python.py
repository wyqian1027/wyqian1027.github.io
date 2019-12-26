# 1. DP O(N^2)

class Solution:
    
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: x[0])
        
        dp = [0]*len(pairs)
        dp[0] = 1
        res = 0
        
        for i in range(1, len(pairs)):
            dp[i] = 1
            curFirst = pairs[i][0]
            for j in range(i):
                if pairs[j][1] < curFirst:
                    dp[i] = max(dp[j] + 1, dp[i]) 
            res = max(res, dp[i])
            
        return res
            
# 2. Greedy Solution O(NlogN)

class Solution:
    
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: x[1])
        
        res = 0
        cur = -float('inf')
        
        for x, y in pairs:
            if cur < x:
                cur = y
                res += 1
                
        return res