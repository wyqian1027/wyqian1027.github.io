class Solution:
    def combinationSum2(self, nums, target):
        
        res = []
        nums.sort()
        
        def dfs(nums, path, cur, res):
            
            if cur == target:
                res.append(path)
              
            for i in range(len(nums)):
                
                if i == 0 or nums[i] != nums[i-1]: 
                    newCur = cur + nums[i]
                    if newCur > target: 
                        return
                    dfs(nums[i+1:], path + [nums[i]], newCur, res)

        dfs(nums, [], 0, res)
        
        return res