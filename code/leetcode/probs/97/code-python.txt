# 1. Reducing 2D DP to 1D DP:

class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        2D DP checking if up to s1[:i] and s2[:j], s3[:i+j] can be formed
        DP[i][j] = (DP[i-1][j] and s1[i-1] == s3[i+j-1]) or (DP[i][j-1] and s2[j-1] == s3[i+j-1])
        
        1D DP:
        1) s1[i] matches and dp[j] true   (UP)
        2) s2[j] matches and dp[j-1] true (LEFT)
        '''

        if len(s1) + len(s2) != len(s3): return False
        
        m, n = len(s1), len(s2)
        dp = [False]*(n+1)
        dp[0] = True

        for j in range(1, n+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, m+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1]

# 2. DFS with Memoization
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        res = {}
        return self.dfs(s1, s2, s3, res)

    def dfs(self, s1, s2, s3, res):
        
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == "" and s2 == "" and s3 == "":
            return True
        if s1 == "":
            return s2 == s3
        if s2 == "":
            return s1 == s3
        
        key = (s1, s2, s3)
        if key in res: return res[key]
        
        ch = s3[0]
        flag = False
        if s2[0] == ch: flag = flag | self.dfs(s1, s2[1:], s3[1:], res)
        if s1[0] == ch: flag = flag | self.dfs(s1[1:], s2, s3[1:], res)
        
        res[key] = flag
        return flag
        
        