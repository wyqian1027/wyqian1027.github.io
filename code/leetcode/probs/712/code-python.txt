class Solution:
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
    
        dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]
        # row is s1
        
        for i in range(len(s1)):
            dp[0][i+1] = dp[0][i] + ord(s1[i])
            
        for i in range(len(s2)):
            dp[i+1][0] = dp[i][0] + ord(s2[i])
            
        for i in range(len(s2)):
            for j in range(len(s1)):
                if s1[j] == s2[i]:
                    dp[i+1][j+1] = dp[i][j]
                
                else:
                    dp[i+1][j+1] = min(dp[i][j+1]+ord(s2[i]), dp[i+1][j]+ord(s1[j]))
            
        return dp[-1][-1]
                    
            
        
        