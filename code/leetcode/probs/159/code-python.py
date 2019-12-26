# key testcase to think about : "abaccc"  -> 4

# 1. RightMost HashMap
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        l = 0
        r = 0
        d = collections.defaultdict() # rightmost position
        maxL = 0
        while r < len(s):
            if len(d) <= 2:
                d[s[r]] = r
                r += 1
            while len(d) > 2:
                if l == d[s[l]]:
                    del d[s[l]]
                l += 1                              
            maxL = max(maxL, r - l)
        return maxL

# 2. Frequency HashMap
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        loc = []
        d = {}   # ch -> incontinuous counts
        
        maxL = 0
        for i, ch in enumerate(s+"$"):
            if ch in d:
                if loc[-1] != ch:
                    d[ch] += 1
                    loc.append(i)
            else:
                if loc:
                    idx = loc[0]
                    maxL = max(maxL, i - idx)
                while len(d) == 2:
                    idx = loc.pop(0)
                    d[s[idx]] -= 1
                    if d[s[idx]] == 0: del d[s[idx]]
                d[ch] = 1
                loc.append(i)  
        return maxL