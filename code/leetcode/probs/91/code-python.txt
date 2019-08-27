class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0]*(len(s)+1) 
        dp[0] = 1
        
        for i in range(len(s)):
            
            ch = s[i]
            idx = i + 1
            if "1" <= ch <= "9":
                dp[idx] += dp[idx-1]
            if i > 0 and '10' <= s[i-1] + ch <= "26":
                dp[idx] += dp[idx-2]
        
        return dp[-1]

# Or reduce to O(1) space
class Solution:
    def numDecodings(self, s: str) -> int:
    
        prev, cur = 0, 1
        
        for i, ch in enumerate(s):
            nxt = 0
            if i - 1 >= 0 and 10 <= int(s[i-1: i+1]) <= 26:
                nxt += prev
            nxt += cur if ch != "0" else 0
            prev, cur = cur, nxt
                
        return cur
            
        