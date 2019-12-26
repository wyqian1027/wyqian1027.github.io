class Solution:
    
    def hIndex(self, citations: List[int]) -> int:
        
        lo, hi = 0, len(citations)-1
        ans = 0
        
        while lo <= hi:
            
            m = lo + (hi-lo)//2
            ct = len(citations) - m
            if citations[m] == ct:
                return ct
            elif citations[m] > ct:
                hi = m - 1
                ans = ct
            else:
                lo = m + 1
        
        return ans
        