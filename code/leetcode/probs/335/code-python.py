class Solution:
    
    def isSelfCrossing(self, x):
        
        a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
        
        for dx in x:
                 
            a, b, c, d, e, f = dx, a, b, c, d, e
            
            # a is always the newest, b is the prev, c is second prev, ...
            
            # print(a, b, c, d, e, f)
            
            # three cases for crossing, could be combined
            
            if (b <= d and a >= c > 0): return True
        
            if (b == d and c == e + a and e > 0): return True
            
            if (d > f > 0 and b <= d and c > e and a >= c - e > 0 and b >= d - f): return True
    
        return False