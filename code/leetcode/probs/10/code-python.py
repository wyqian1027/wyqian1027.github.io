# 1. Recursion: O(2^(T+P))

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return s == ""
        
        firstMatch = bool(s) and p[0] in {s[0], '.'}
        
        if len(p) >= 2 and p[1] == '*':
            # case 1. erase s[0] with * 
            # case 2. repeat prev character, provided firstMatch True
            # ps: ** is invalid/excluded
            return (self.isMatch(s, p[2:])) or \
                   (firstMatch and self.isMatch(s[1:], p)) 
        else:
            return firstMatch and self.isMatch(s[1:], p[1:])

# 1. DP  O(TP)

class Solution:
    def isMatch(self, s, p):
        cache = {}
        def dp(i, j):
            if (i, j) not in cache:
                if j == len(p):
                    ans = i == len(s)
                else:
                    firstMatch = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == "*":
                        ans = dp(i, j+2) or firstMatch and dp(i+1, j)
                    else:
                        ans = firstMatch and dp(i+1, j+1)
                cache[(i,j)] = ans
            return cache[(i,j)]
        return dp(0, 0)

