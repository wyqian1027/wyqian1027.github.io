class Solution:

    def combine(self, n, k):
        
        res = []
        nums = [i+1 for i in range(n)]
        
        def helper(nums, k, path, res):
            if k == 0:
                res.append(path)
                return
            for i in range(len(nums)-k+1):
                helper(nums[i+1:], k-1, path + [nums[i]], res)

        helper(nums, k, [], res)
        return res   