class Solution:
    def combinationSum(self, nums, target):
        
        res = []

        def dfs(nums, path, cur, res):
            
            if cur > target:
                return
            
            if cur == target:
                res.append(path)
                
            for i in range(len(nums)):
                dfs(nums[i:], path + [nums[i]], cur + nums[i], res)
                         
        dfs(nums, [], 0, res)
        
        return res