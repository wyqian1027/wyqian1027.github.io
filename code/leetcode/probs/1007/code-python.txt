class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        n = len(A)
        cand = [A[0], B[0]]
        
        min_swap = float('inf')
        for x in cand:
            rotation_A = rotation_B = 0
            possible = True
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    possible = False
                    break
                if A[i] != x: rotation_A += 1
                if B[i] != x: rotation_B += 1
            if possible: 
                min_swap = min(min_swap, rotation_A, rotation_B)
                break
        
        return min_swap if min_swap != float('inf') else -1