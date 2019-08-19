class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        n = len(A)
        i, j = 0, n - 1
        while i+1 < n and  A[i] < A[i+1]: i += 1
        while j-1 >= 0 and A[j-1] > A[j]: j -= 1
        return 0 < i == j < n - 1

#   Alternative:
#         while i+1 < n and A[i] < A[i+1]: i += 1
#         if i == 0 or i == n-1: return False
#         while i+1 < n and A[i] > A[i+1]: i += 1
#         return i == n - 1