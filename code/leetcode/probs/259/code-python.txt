class Solution:
    def threeSumSmaller(self, A, target):
        
        if len(A) < 3: return 0
        A.sort()
        res = 0
        
        for i in range(2, len(A)):
            
            l, r = 0, i-1
            
            while l < r:
                
                if A[l] + A[r] + A[i] < target:
                    
                    res += r - l
                    l += 1
                
                else:
                    
                    r -= 1            
            
        return res
    
    
