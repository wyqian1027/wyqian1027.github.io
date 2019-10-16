class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        m = n + 1
        
        for i in range(n):
            index = (nums[i] % m) - 1
            nums[index] += m
        
        res = []
        for i, num in enumerate(nums):
            if num < m:
                res.append(i+1)
        
        return res