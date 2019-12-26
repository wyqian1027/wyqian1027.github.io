# O(N^2) Solution with Swapping
class Solution:
    def minSwapsCouples(self, A: List[int]) -> int:
        
        count = 0
        n = len(A)
        for i in range(0, n, 2):
            k1 = A[i]
            k2 = k1^1
            if A[i+1] != k2:
                for j in range(i+2, len(A)):
                    if A[j] == k2:
                        A[j], A[i+1] = A[i+1], A[j]
                        count += 1
                        break
        return count        