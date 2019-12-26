class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
    
        if not nums: return 0
        
        if len(nums) <= 2: return len(nums)
        
        i = 2  # read
        j = 2  # write
        
        while i < len(nums):
            
            cur = nums[i]
            prev = nums[j-1]
            prev2 = nums[j-2]
            
            # if cur != prev:
            #     nums[j] = cur
            #     j += 1
            # elif prev != prev2:
            #     nums[j] = cur
            #     j += 1
            
            if cur != prev2:
                nums[j] = cur
                j+= 1
                
            i += 1
                
        return j
            