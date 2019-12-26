# O(lgN) Binary Search Solution

class Solution:
    def singleNonDuplicate(self, A: List[int]) -> int:
        lo, hi = 0, len(A)-1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if mid > 0 and A[mid] == A[mid - 1]:
                if (mid - 1 - lo) % 2 == 1:
                    hi = mid - 2
                else:
                    lo = mid + 1            
            elif mid + 1 < len(A) and A[mid] == A[mid+1]:
                if (hi - (mid + 1)) % 2 == 1:
                    lo = mid + 2
                else:
                    hi = mid - 1       
            else:
                return A[mid]     
                
# Smart Usage of mid^1 to get its partner
class Solution:
    def singleNonDuplicate(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = lo + (hi - lo)//2
            if A[mid] == A[mid^1]:
                lo = mid + 1
            else:
                hi = mid
        return A[lo]