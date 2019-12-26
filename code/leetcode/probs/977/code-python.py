# Two pointers O(N)
from bisect import bisect_left as bl

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        start = bl(A, 0)
        l, r = start - 1, start
        res = []
        
        while l >= 0 and r < len(A):
            if abs(A[l]) <= abs(A[r]):
                res.append(A[l]*A[l])
                l -= 1
            else:
                res.append(A[r]*A[r])
                r += 1
        while r < len(A):
            res.append(A[r]*A[r])
            r += 1
        while l >= 0:
            res.append(A[l]*A[l])
            l -= 1
        
        return res
            