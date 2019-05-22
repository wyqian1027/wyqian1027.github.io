# DP 1D Python, since only use prev DP, no need for DP 2D

class Solution:
    
    def findTargetSumWays(self, nums, target):
        
        if target > 1000 or target < -1000: return 0
        
        dp = {}
        
        dp[nums[0]] = dp.get(nums[0], 0) + 1
        dp[-nums[0]] = dp.get(-nums[0], 0) + 1
            
        
        for i in range(1, len(nums)):
            newDP = {}
            for prevS, count in dp.items():
                newDP[prevS + nums[i]] = newDP.get(prevS + nums[i], 0) + count
                newDP[prevS - nums[i]] = newDP.get(prevS - nums[i], 0) + count
            dp = newDP
            
        return dp.get(target, 0)