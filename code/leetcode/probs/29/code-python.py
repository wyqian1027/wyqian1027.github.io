class Solution:
    def divide(self, A: int, B: int) -> int:
        if A == - (1 << 31) and B == -1: return (1 << 31) - 1
        a = abs(A); b = abs(B); res = 0
        for x in range(31, -1, -1):
            if a - (b << x) >= 0:
                res += 1 << x
                a -= (b << x)
        
        return res if (A > 0) == (B > 0) else -res
