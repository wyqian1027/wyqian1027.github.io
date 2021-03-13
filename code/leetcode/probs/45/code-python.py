class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        # current range [l, r]
        l = 0; r = nums[0]; numJumps = 1
        while r < len(nums)-1:
            newR = max([i+nums[i] for i in range(l, r+1)])
            l = r+1
            r = newR
            numJumps += 1
        return numJumps
