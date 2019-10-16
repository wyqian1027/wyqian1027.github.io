from heapq import *

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        
        workers = [[wage[i]/quality[i] , wage[i], quality[i]] 
                   for i in range(len(quality))]
        
        workers.sort()
        
        ans = float('inf')
        sumq = 0
        h = []    # max heap so that we rid of high quality workers
        
        for ratio, w, q in workers:
            heappush(h, -q)
            sumq += q
            
            if len(h) > K:
                sumq += heappop(h)
                
            if len(h) == K:
                ans = min(ans, sumq*ratio)  # this ratio will work for all workers so far
            
        return ans 