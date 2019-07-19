# O(NlgN)

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        
        i = 1
        while i < n - 1:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2
            
# O(N) Greedy using one boolean value to check

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        up = False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if up:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                up ^= True
            else:
                if not up:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                up ^= True