# DP

class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        
        mines = set([tuple(mine) for mine in mines])
        max_ones = 0
        dp = [[0]*N for _ in range(N)]
        
        for i in range(N):
            count = 0
            for j in range(N):                  # checking left
                count = 0 if (i, j) in mines else count + 1
                dp[i][j] = count
            
            count = 0 
            for j in range(N-1, -1, -1):        # checking right
                count = 0 if (i, j) in mines else count + 1
                if count < dp[i][j]: dp[i][j] = count
        
        for j in range(N):
            count = 0
            for i in range(N):                  # checking up
                count = 0 if (i, j) in mines else count + 1
                if count < dp[i][j]: dp[i][j] = count
            
            count = 0
            for i in range(N-1, -1, -1):        # checking bottom
                count = 0 if (i, j) in mines else count + 1
                if count < dp[i][j]: dp[i][j] = count
                    
                max_ones = max(max_ones, dp[i][j])
                
        return max_ones
        