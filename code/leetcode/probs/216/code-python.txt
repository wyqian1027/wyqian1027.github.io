class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = list(range(1, 10))
        res = []
        
        def dfs(nums, path, k, target, res):
            
            if k < 0 or sum(path) > target:
                return
            
            if k == 0 and sum(path) == target:
                res.append(path)
                return
            
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]], k-1, target, res)
                
        dfs(nums, [], k, n, res)
    
        return res
        