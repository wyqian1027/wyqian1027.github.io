# From 2D to 1D, Knapsack solution

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        knapsack problem: dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]] if (j-nums[i] >= 0)
        """ 
        total = sum(nums)
        if total % 2 == 1: return False
        
        total = total // 2
        
        dp = [[False]*(total+1) for _ in range(len(nums)+1)]
        for i in range(len(dp)): dp[i][0] = True
        
        
        # each dp[i][j] computes the whether sum value = j-1 can be obtained with first i-1 items
        # one extra space in i, j is included for null sum and null items
        
        for i in range(1, len(nums)+1):
            for j in range(1, total+1):
                dp[i][j] = dp[i-1][j]             # without adding this number nums[i-1] to the set
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]  # with adding nums[i-1] to the set
        return dp[-1][-1]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        knapsack problem: dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]] if (j-nums[i] >= 0)
        """ 
        total = sum(nums)
        if total % 2 == 1: return False
        
        total = total // 2
        
        dp = [False]*(total+1)
        dp[0] = True
                
        for i in range(1, len(nums)+1):
            for j in range(total, -1, -1):
                if j - nums[i-1] >= 0:
                    dp[j] = dp[j] or dp[j-nums[i-1]] 
        return dp[-1]
                