# 1. O(1) space SUM[i:j] = SUM[:j] - SUM[:i-1]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        largestSum = float('-inf')
        lowestSum = 0  # incase start from 0th element
        s = 0
        for num in nums:
            s += num
            largestSum = max(largestSum, s - lowestSum)
            lowestSum = min(lowestSum, s)
        return largestSum
        
# 2. DP
# DP[i] = maximum subarray ends at index i, basically we traverse and choose if to include previous dp[i-1]

class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0]*len(nums)
        dp[0] = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]) + nums[i]
            res = max(res, dp[i])
            
        return res 
        