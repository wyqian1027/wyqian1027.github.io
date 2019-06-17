class Solution:
    
    def threeSum(self, A: List[int]) -> List[List[int]]:
        
        if len(A) < 3: return []
        A.sort()
        if sum(A[-3:]) < 0 or sum(A[:3]) > 0: return []
        res = []
        
        for i in range(len(A) - 2):
            if i != 0 and A[i] == A[i-1]:
                continue
            
            left, right = i + 1, len(A) - 1
            while left < right:
                s = A[i] + A[left] + A[right]                     
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    res.append([A[i], A[left], A[right]])
                    while left < right and A[left] == A[left+1]:
                        left += 1
                    while left < right and A[right] == A[right-1]: 
                        right -= 1
                    left += 1
                    right -= 1
        return res