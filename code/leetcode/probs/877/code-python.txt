class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        
        n = len(piles)
        
        cache = {}
        
        def dp(i, j):  # find max stones from piles[i] to piles[j], inclusive
            
            if i > j: return 0
            
            if (i, j) in cache: return cache[(i,j)]
            
            turn = n - (j-i+1)
            
            if turn % 2 == 0: # alex's turn
                
                ans = max(piles[i] + dp(i+1, j), piles[j] + dp(i, j-1))
                
            else:  # lee's turn
                
                ans = min(-piles[i] + dp(i+1, j), -piles[j] + dp(i, j-1))
                
            cache[(i,j)] = ans
            
            return ans
        
        return dp(0, n-1) > 0
        