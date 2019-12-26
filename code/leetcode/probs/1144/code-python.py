class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        nums = [float('inf')] + nums + [float('inf')]
        movesOdd, movesEven = 0, 0
        for i in range(1, len(nums)-1):
            if i % 2 == 1:
                movesOdd += max(0, nums[i] - min(nums[i-1], nums[i+1]) + 1)
            else:
                movesEven += max(0, nums[i] - min(nums[i-1], nums[i+1]) + 1)
        return min(movesOdd, movesEven)
            