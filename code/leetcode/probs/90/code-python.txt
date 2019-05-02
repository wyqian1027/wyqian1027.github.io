class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        def dfs(nums, path, res):
            
            res.append(path)
            
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    dfs(nums[i+1:], path + [nums[i]], res)
            
        dfs(nums, [], res)
        
        return res
                
            