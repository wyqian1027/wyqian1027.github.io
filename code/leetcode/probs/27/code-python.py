# Two Pointers

class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not nums: return 0
        
        i = 0
        l = len(nums)
        
        while i < l:
            
            if nums[i] == val:
                nums[i], nums[l-1] = nums[l-1], nums[i]
                l -= 1
            else:
                i += 1
        
        return l
                
                
        