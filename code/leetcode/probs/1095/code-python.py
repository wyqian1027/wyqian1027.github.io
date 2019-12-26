# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        
        self.length = arr.length()
                
        ind = self.findPeak(arr, 0, self.length - 1)
                
        ans = self.binarySearch(target, arr, 0, ind, False)
        if ans != -1: return ans
        
        ans = self.binarySearch(target, arr, ind, self.length - 1, True)
        if ans != -1: return ans
        
        return -1
    
    def findPeak(self, arr, lo, hi):
        
        while lo < hi:
            m = lo + (hi - lo) // 2

            if arr.get(m) < arr.get(m+1):
                lo = m + 1
            else:
                hi = m
        
        return lo       
        
        
    def binarySearch(self, target, arr, start, end, inverted):
        
        if not inverted:
            while start <= end:
                m = start + (end - start) // 2
                mid = arr.get(m)
                if mid == target:
                    return m
                elif mid < target:
                    start = m + 1
                else:
                    end = m -1
        else:
            while start <= end:
                m = start + (end - start) // 2
                mid = arr.get(m)
                if mid == target:
                    return m
                elif mid < target:
                    end = m - 1
                else:
                    start = m + 1            
        
        return -1