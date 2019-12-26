from functools import lru_cache

class Solution:
    
    @lru_cache(None)
    def divisorGame(self, N: int) -> bool:

        for x in range(1, N//2+1):
            if N % x == 0 and self.divisorGame(N-x) == False:
                return True
            
        return False