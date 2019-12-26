# O(NLgN) Heap solution:
from heapq import *

class Solution:
    def maxAbsValExpr(self, A: List[int], B: List[int]) -> int:
            
        # max heap
        h1 = [(-(A[0] + B[0]), 0)]  
        h2 = [(-(A[0] - B[0]), 0)]  
        h3 = [(-(-A[0] - B[0]), 0)] 
        h4 = [(-(-A[0] + B[0]), 0)] 
        
        ans = 0
        
        for k in range(1, len(A)):
            x = A[k]
            y = B[k]
            s1, i1 = h1[0]
            s2, i2 = h2[0]
            s3, i3 = h3[0]
            s4, i4 = h4[0]
            ans = max(ans, -s1 - x - y + k - i1)
            ans = max(ans, -s2 - x + y + k - i2)
            ans = max(ans, -s3 + x + y + k - i3)
            ans = max(ans, -s4 + x - y + k - i4)
            
            heappush(h1, (-(x+y), k))
            heappush(h2, (-(x-y), k))
            heappush(h3, (-(-x-y), k))
            heappush(h4, (-(-x+y), k))
        
        return ans

# O(N) Math Solution

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        
        l1, l2, l3, l4 = [], [], [], []
        
        for i in range(len(arr1)):
            a = arr1[i]
            b = arr2[i]
            l1 += [   a + b + i ]
            l2 += [   a - b + i ]
            l3 += [ - a + b + i ]
            l4 += [ - a - b + i ]
        
        ans = 0
        ans = max(ans, max(l1) - min(l1))
        ans = max(ans, max(l2) - min(l2))
        ans = max(ans, max(l3) - min(l3))
        ans = max(ans, max(l4) - min(l4))
        
        return ans