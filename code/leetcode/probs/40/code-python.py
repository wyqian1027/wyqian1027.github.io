class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        def dfs(start, path, target):
            if target < 0: return
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i-1]: continue
                dfs(i+1, path + [nums[i]], target-nums[i])
        
        dfs(0, [], target)
        return res
