class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p = 0, 0
        while p < len(nums):
            if nums[p] != 0:
                nums[p], nums[p1] = nums[p1], nums[p]
                p1 += 1
            p += 1