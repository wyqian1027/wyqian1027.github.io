class Solution:
    
    def findNumberOfLIS(self, nums: List[int]) -> int:
    
        if not nums: return 0
        
        dp = [0]*len(nums)
        counts = [0]*len(nums)
        dp[0] = 1
        counts[0] = 1
        maxLen = 1
        ans = 1
    
        for i in range(1, len(nums)):
            res = 1 # current length
            ct = 1   # current count
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 == res:
                        ct += counts[j]
                    elif dp[j] + 1 > res:
                        ct = counts[j]
                        res = dp[j] + 1
                    res = max(res, dp[j] + 1)
            dp[i] = res
            counts[i] = ct
            if res == maxLen:
                ans += ct
            elif res > maxLen:
                ans = ct   
                maxLen = res

        return ans