class Solution:
    def minHeightShelves(self, A: List[List[int]], shelfWidth: int) -> int:
        
        if not A or len(A) == 0: return 0
        
        dp = [float('inf') for _ in range(len(A)+1)]
        dp[0] = 0
        
        for i in range(0, len(A)):
            
            width = A[i][0]
            height = A[i][1]
            dp[i+1] = height + dp[i]
            for j in range(i-1, -1, -1):
                if A[j][0] + width <= shelfWidth:
                    width += A[j][0]
                    height = max(height, A[j][1])
                    dp[i+1] = min(dp[i+1], dp[j] + height)
                else:
                    break
        
        return dp[-1]