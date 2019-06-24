# 1. Adapting from Meeting Room II:
from heapq import heappush, heappop

class Solution:
    
    def carPooling(self, trips: List[List[int]], cap: int) -> bool:
        
        trips.sort(key = lambda x: x[1]) # sort by start distance
        
        h = []       
        num = 0
        c = 0
        
        for trip in trips:
            
            while h and h[0][0] <= trip[1]:
                num -= heappop(h)[1]           # get rid of old passengers
                
            num += trip[0]                     # add new passenger
            heappush(h, (trip[2], trip[0], c))
            c += 1
            if num > cap: return False
            
        return True
        
# 2. Simplify using HashMap or even Array to achieve O(N) or O(1)

class Solution:
    
    def carPooling(self, trips, cap):
        
        d = {}
        
        for n, s, e in trips:
            d[s] = d.get(s, 0) + n
            d[e] = d.get(e, 0) - n
            
        for k in sorted(d.keys()):
            cap -= d[k]
            if cap < 0: return False
        
        return True

class Solution:

    def carPooling(self, trips, cap):
        
        record = [0]*1001
        
        for n, s, e in trips:
            record[s] += n
            record[e] -= n
        
        for r in record:
            cap -= r
            if cap < 0: return False
        
        return True