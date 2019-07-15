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