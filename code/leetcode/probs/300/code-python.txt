# O(N^2) Approach. DP stores the maximum length of subsequence ended at each index

class Solution:
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums: return 0
        dp = [0]*len(nums)
        maxLIS = 0
        
        for i in range(len(nums)):
            res = 0
            for j in range(0, i):
                if nums[j] < nums[i]: res = max(res, dp[j])
            dp[i] = res + 1
            maxLIS = max(maxLIS, dp[i])
            
        return maxLIS

# O(NlogN). DP maps the subsequence length to the least ended number
# DP length = max subsequence length
# DP[i] represents the subsequence of length i, with the smallest ending number.

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        dp = [nums[0]]
        
        for i in range(len(nums)):
            
            index = bisect.bisect_left(dp, nums[i]) # use left, because of possible repetition.
            
            if (index == len(dp)):
                dp.append(nums[i])
            else:
                dp[index] = nums[i]   # must be new minimum
                
        return len(dp)