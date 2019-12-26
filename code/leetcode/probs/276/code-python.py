class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        if n == 0: return 0
        
        same, diff = 0, k
        
        for _ in range(n-1):
            nextSame = diff*1
            nextDiff = same*(k-1) + diff*(k-1)
            same, diff = nextSame, nextDiff
        
        return same + diff