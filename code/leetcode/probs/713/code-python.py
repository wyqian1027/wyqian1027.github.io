class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1: return 0
        
        cur = 1
        left = 0
        total = 0
        
        for right, val in enumerate(nums):
            cur = cur*val
            while cur >= k:
                cur //= nums[left]
                left += 1
            total += right - left + 1
        
        return total