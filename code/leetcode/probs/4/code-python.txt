class Solution:
    
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        
        m, n = len(A), len(B)
        if m > n:
            m, n = n, m
            A, B = B, A
        
        imin = 0
        imax = m
        
        while True:
            
            i = (imin + imax)//2
            j = (m+n+1)//2 - i
            
            if i != 0 and A[i-1] > B[j]:
                imax = i - 1
            
            elif i < m and B[j-1] > A[i]:
                imin = i + 1
                
            else:
                
                if i == 0:
                    maxLeft = B[j-1]
                elif j == 0: 
                    maxLeft = A[i-1]
                else:
                    maxLeft = max(A[i-1], B[j-1])
                
                if (m+n) % 2 == 1:
                    return maxLeft
        
                if i == m:
                    maxRight = B[j]
                elif j == n:
                    maxRight = A[i]
                else:
                    maxRight = min(A[i], B[j])
                
                return (maxLeft + maxRight) / 2.0