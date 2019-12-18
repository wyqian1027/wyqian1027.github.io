class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        m, n = len(mat), len(mat[0])
        dp =  [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]
        
        max_t = 0
        s = min(m, n)
        
        for i in range(m):
            for j in range(n):
                min_k = max_t
                for k in range(min_k, s):
                    if i + k >= m or j + k >= n: break
                    i2 = i + k
                    j2 = j + k
                    area = dp[i2+1][j2+1] - dp[i2+1][j] - dp[i][j2+1] + dp[i][j]
                    if area > threshold:
                        break
                    else:
                        max_t = max(k + 1, max_t)
        
        return max_t