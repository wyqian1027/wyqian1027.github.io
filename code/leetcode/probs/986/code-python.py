class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        def isOverlap(a, b):
            return a[1] >= b[0] and a[0] <= b[1]
        
        i = j = 0
        ans = []
                
        while i < len(A) and j < len(B):
            a = A[i]
            b = B[j]
            
            if isOverlap(a, b):
                ans.append([max(a[0], b[0]), min(a[1], b[1])])
            
            if a[1] <= b[1]:
                i += 1
            else:
                j += 1
        
        return ans