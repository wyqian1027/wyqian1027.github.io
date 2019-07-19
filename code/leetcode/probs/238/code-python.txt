class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        s = 1
        for i in range(n):
            res[i] *= s
            s *= nums[i]
        s = 1
        for i in reversed(range(n)):
            res[i] *= s
            s *= nums[i]
        return res