class Solution:
    def maxEnvelopes(self, dolls: List[List[int]]) -> int:
        
        dolls.sort(key=lambda doll: (doll[0], -doll[1]))
        dp = [0]*len(dolls)
        l = 0
        
        for doll in dolls:
            index = bisect.bisect_left(dp, doll[1], 0, l)
            dp[index] = doll[1]
            if index == l: l+=1
                
        return l