class Solution:
    def numDecodings(self, s: str) -> int:
        
        d = {}   # index -> d[digit] = count 
        d[-1] = {1: 1}
        MOD = 10**9 + 7
        
        for i, ch in enumerate(s):
            
            # if i - 3 in d: del d[i-3]
            d[i] = {}
            res = 0
            last_sum = sum(d[i-1].values()) % MOD
            
            if ch != "*":
                d[i][int(ch)] = last_sum if ch != "0" else 0
                
            else:
                for x in range(1, 10):
                    d[i][x] = last_sum
                    
            if i - 1 >= 0:
                last_last_sum = sum(d[i-2].values()) % MOD
                for x in d[i-1]:
                    for y in d[i]:
                        if 10 <= 10*x + y <= 26:
                            d[i][y] = (d[i].get(y, 0) + last_last_sum) % MOD
            
        return sum(d[len(s)-1].values()) % MOD 

# Or better using 1D DP
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        MOD = 10**9 + 7
        dp = [1] + [0]*len(s)
        
        for i in range(len(s)):
            if s[i] == "*":
                dp[i+1] = 9*dp[i]
                if i - 1 >= 0 and s[i-1] == "1":
                    dp[i+1] = (dp[i+1] + 9*dp[i-1]) % MOD
                elif i - 1 >= 0 and s[i-1] == "2":
                    dp[i+1] = (dp[i+1] + 6*dp[i-1]) % MOD
                elif i - 1 >= 0 and s[i-1] == "*":
                    dp[i+1] = (dp[i+1] + 15*dp[i-1]) % MOD
            else:
                dp[i+1] = dp[i] if s[i] != "0" else 0
                if i - 1 >= 0 and s[i-1] == "1":
                    dp[i+1] = (dp[i+1] + dp[i-1]) % MOD
                elif i - 1 >= 0 and s[i-1] == "2" and s[i] <= "6":
                    dp[i+1] = (dp[i+1] + dp[i-1]) % MOD
                elif i - 1 >= 0 and s[i-1] == "*":
                    if s[i] <= "6":
                        dp[i+1] = (dp[i+1] + 2*dp[i-1]) % MOD
                    else:
                        dp[i+1] = (dp[i+1] + dp[i-1]) % MOD
        
        return dp[-1]
                    
        
        
        
        
        
        
        
        