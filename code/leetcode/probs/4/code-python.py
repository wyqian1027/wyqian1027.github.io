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

# updated solution: 04/10/2021
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        '''
        - Divide A and B into two equal parts (suppose B is longer)
        A = A[0]...A[i-1]   |     A[i]...A[m-1]
        B = B[0]...B[j-1]   |     B[j]...B[n-1]
        - We need to find i, j to satisfy the conditions:
        (1) i + j = m - i + n - j
        (2) A[i-1] <= B[j]
        (3) B[j-1] <= A[i]
        '''
        m = len(A); n = len(B)
        if m == 0: return (B[n//2] + B[(n-1)//2])/2
        if n == 0: return (A[m//2] + A[(m-1)//2])/2
        
        if m > n:
            m, n = n, m
            A, B = B, A
    
        l = 0; r = m
        
        while l <= r:
            i = l + (r-l)//2
            j = (m+n)//2 - i
            if i > 0 and A[i-1] > B[j]:
                r = i-1
            elif i < m and B[j-1] > A[i]:
                l = i+1
            else: # A[i-1] <= B[j] and B[j-1] <= A[i]
                break
        
        iLeft = A[i-1] if i > 0 else float('-inf')
        iNum = A[i] if i < m else float('inf')
        jLeft = B[j-1] if j > 0 else float('-inf')
        jNum = B[j] if j < n else float('inf')
        maxLeft = max(iLeft, jLeft)
        minRight = min(iNum, jNum) 
        
        return minRight if (n+m) % 2 == 1 else (maxLeft + minRight)/2
        
