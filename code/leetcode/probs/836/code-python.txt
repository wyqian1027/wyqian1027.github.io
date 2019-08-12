# The hard way:
class Solution:
    def isRectangleOverlap(self, A: List[int], B: List[int]) -> bool:
        if A[0] < B[2] and A[1] < B[3] and A[2] > B[0] and A[3] > B[1]:
            return True
        A, B = B, A
        if A[0] < B[2] and A[1] < B[3] and A[2] > B[0] and A[3] > B[1]:
            return True
        
        return False

# Or think of the opposite case:
class Solution:
    def isRectangleOverlap(self, A: List[int], B: List[int]) -> bool:
        if A[2] <= B[0] or A[0] >= B[2] or \
        A[1] >= B[3] or A[3] <= B[1]:
            return False
        return True