class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [False]*(n+1)
        st = set(wordDict)
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in st:
                    dp[i] = True
                    break
        return dp[-1]