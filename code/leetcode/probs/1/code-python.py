class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        
        for i, x in enumerate(nums):
            
            if x in d:
                
                return [d[x], i]
            
            else:
                
                d[target - x] = i
                
        return [-1, -1]