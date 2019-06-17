class Solution:
    
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if k < 0 or t < 0: return False
        
        bucket = {}
        
        for i, x in enumerate(nums):
            
            idx = x // (t + 1)
            
            if idx in bucket:
                return True
            if idx-1 in bucket and bucket[idx-1] + t >= x:
                return True
            if idx+1 in bucket and bucket[idx+1] - t <= x:
                return True
            
            bucket[idx] = x
            if i - k >= 0:
                del bucket[nums[i-k]//(t+1)]
        
        return False