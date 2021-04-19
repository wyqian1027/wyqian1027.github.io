class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        def dfs(i, path):
            res.append(path[:])          
            for j in range(i, n):
                if j != i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                dfs(j+1, path)
                path.pop()
                
        dfs(0, [])
        return res
