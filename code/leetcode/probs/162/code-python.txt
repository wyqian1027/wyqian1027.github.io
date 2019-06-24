// 1. Just Compare mid and mid + 1
class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        
        lo, hi = 0, len(A) - 1
        
        while lo < hi:
            
            mid = lo + (hi - lo)//2
            if A[mid] > A[mid+1]:
                hi = mid
            else:
                lo = mid + 1
        
        return lo
        
// 2. More Verbose
class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        
        lo, hi = 0, len(A) - 1
        
        while lo < hi:
            
            mid = lo + (hi - lo)//2
            if A[max(mid-1, 0)] <= A[mid] and A[mid] >= A[min(mid+1, len(A) -1)]:
                return mid
            elif A[mid-1] > A[mid] and A[mid] > A[mid+1]:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo