class Solution:

    def rob(self, H):
        
        if not H: return 0
        
        if len(H) <= 3: return max(H)
        
        def rob1(H):
        
            if not H: return 0

            pre, cur = 0, H[0]

            for i in range(1, len(H)):

                pre, cur = cur, max(cur, pre + H[i])

            return cur
        
        return max(rob1(H[1:]), rob1(H[:-1]))