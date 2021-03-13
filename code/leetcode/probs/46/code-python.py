class Solution:
    def permute(self, nums):
        res = []       
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path + [nums[i]], res)
        dfs(nums, [], res)
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(nums, taken, path):
            if len(path) == n:
                res.append(path[:])
                return
            for i, num in enumerate(nums):
                if not taken[i]:
                    taken[i] = True
                    path.append(num)
                    dfs(nums, taken, path)
                    path.pop()
                    taken[i] = False
        dfs(nums, [False]*n, [])
        return res
                
