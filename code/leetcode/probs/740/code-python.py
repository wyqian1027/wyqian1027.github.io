class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:
    
        array = [0]*20001
        
        for n in nums:
            array[n] += n
        
        prev = cur = 0
        
        for x in array:
            
            prev, cur = cur, max(prev + x, cur)
            
        return max(prev, cur)
        