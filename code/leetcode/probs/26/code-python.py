class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        i, j = 1, 0
        
        while i < len(nums):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
            i += 1
        
        return j + 1