class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = float('-inf')
        
        p = 1
        for i in range(len(nums)):
            if p == 0:
                p = nums[i]
            else:
                p *= nums[i]
            maxP = max(maxP, p)
            
        p = 1
        for i in range(len(nums)-1, -1, -1):
            if p == 0:
                p = nums[i]
            else:
                p *= nums[i]
            maxP = max(maxP, p)
        return maxP