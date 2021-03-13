class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = maxReach = 0
        while i < len(nums) and maxReach < len(nums)-1:
            if i > maxReach:
                return False
            maxReach = max(maxReach, i+nums[i])
            i += 1
        return True
