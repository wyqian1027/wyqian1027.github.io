class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = [0]*n
        nums.sort()
        index = (n+1) // 2
        res[0::2] = nums[:index][::-1]
        res[1::2] = nums[index:][::-1]
        nums[:] = res[:]