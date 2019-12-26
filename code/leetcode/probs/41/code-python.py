# Both Solutions are O(N) Time, O(1) Space
# Use Array itself as HashMap

class Solution:
    
    def firstMissingPositive(self, A: List[int]) -> int:
        
        n = len(A)
        
        for i, num in enumerate(A):
            if num > n or num < 0: A[i] = 0
        
        for i, num in enumerate(A):
            if num != 0:
                idx = (num % (n+1)) - 1
                A[idx] += (n+1)
        
        for i, num in enumerate(A):
            if num < (n+1):
                return (i+1)
        
        return n+1

# Use Swapping

class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        
        n = len(A)
        
        for i in range(len(A)):
            while 0 < A[i] <= n and A[A[i]-1] != A[i]:
                A[A[i]-1], A[i] = A[i], A[A[i]-1]
                
        for i, num in enumerate(A):
            if num != i+1:
                return i+1
        
        return n+1