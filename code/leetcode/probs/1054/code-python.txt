from heapq import *
from collections import Counter, deque
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d = Counter(barcodes)
        pq = []
        for key, count in d.items():
            heappush(pq, (-count, key))
        
        res = []
        store = deque()
        pos = 0
        while pq:
            c, key = heappop(pq)
            res.append(key)
            if c + 1 != 0:
                store.append((pos, c+1, key))
            while store and pos >= store[0][0] + 1:
                _, c, key = store.popleft()
                heappush(pq, (c, key))
            pos += 1
        return res
            
                
        