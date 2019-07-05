# 1. Bit Solution O(N) time, O(1) space.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for x in nums:
            s ^= x
        return s