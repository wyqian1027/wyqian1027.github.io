# O(1) time, O(n) space
class NumArray:

    def __init__(self, nums: List[int]):
        
        self.res = [0]*(len(nums) + 1)
        for i in range(len(nums)):
            self.res[i+1] = self.res[i]+nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.res[j+1] - self.res[i]