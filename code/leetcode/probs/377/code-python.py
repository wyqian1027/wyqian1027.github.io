#1. Backtracking
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        res = []
        nums.sort()
        
        def dfs(nums, target, path, res):
            
            if target == 0:
                res.append(path)
                return
            
            if target < 0:
                return
            
            for i, x in enumerate(nums):
                if target - x < 0: break
                dfs(nums, target - x, path + [x], res)
                
        dfs(nums, target, [], res)
        
        return len(res)
        
#2. DP
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0]*(target+1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if (i-num >= 0):
                    dp[i] += dp[i-num]
                
        return dp[-1]

#3. Improved DP
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        dp = [0]*(target+1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if (num > i): break
                dp[i] += dp[i-num]
                
        return dp[-1]