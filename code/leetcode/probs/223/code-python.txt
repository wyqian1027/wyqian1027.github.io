class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        left   = max(A, E)
        right  = max(left, min(C, G))
        top    = min(D, H)
        bottom = min(top, max(B, F))
        
        overlap = (right - left) * (top - bottom)
        
        return (D-B)*(C-A) + (H-F) *(G-E) - overlap