class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        vals = [0]*len(hours)
        cur = 0
        d = {}
        for i, x in enumerate(hours):
            if x > 8:
                cur += 1
            else:
                cur -= 1
            vals[i] = cur
            if cur not in d:
                d[cur] = i
        
        longest = 0
        
        for i in range(len(vals)):
            x = vals[i]
            if x > 0:
                longest = i+1
            if x - 1 in d:
                longest = max(longest, i- d[x-1])
        
        return longest

# or more concisely
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        seen = {}
        score = ans = 0
        for i, hour in enumerate(hours):
            score = score + 1 if hour > 8 else score - 1
            if score > 0:
                ans = i + 1
            elif score - 1 in seen:
                ans = max(ans, i - seen[score-1])
            if score not in seen:
                seen[score] = i
        return ans