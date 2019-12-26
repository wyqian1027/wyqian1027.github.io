# 1 Cyclic Rotation

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        if not nums or k == 0: return
        
        n = len(nums)
        i = k
        start = 0
        tmp = nums[0]
        
        for _ in range(len(nums)):
            if i != start:
                nums[i], tmp = tmp, nums[i]
                i = (i + k) % n
            else:
                nums[i] = tmp
                tmp = nums[(i+1) % n]
                start = (i + 1) % n
                i = (start + k) % n

        return