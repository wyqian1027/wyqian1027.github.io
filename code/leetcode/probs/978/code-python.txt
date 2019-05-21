class Solution:
    
    def maxTurbulenceSize(self, A: List[int]) -> int:
        
        inc = dec = res = 1
        
        for i in range(1, len(A)):
            
            if A[i-1] > A[i]:
                dec = inc + 1
                inc = 1
            elif A[i-1] < A[i]:
                inc = dec + 1
                dec = 1
            else:
                inc = dec = 1
        
            res = max(res, inc, dec)
        
        return res
                