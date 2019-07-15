# 1. PriorityQueue Dijkstra

from heapq import heappop, heappush

class Solution:
    
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        # min heap, dijkstra 
        
        h = [[0, 0, 0]]
        def dist(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        seen = set()
        
        while h:
            cost, i, visited = heappop(h)
            if (i, visited) in seen: continue
            seen.add((i, visited))
            if i == len(workers): return cost
            for j in range(len(bikes)):
                if visited & (1 << j) == 0:
                    heappush(h, [cost + dist(bikes[j], workers[i]), i+1, visited | (1 << j)])
        return -1
        
# 2. DP with Cache (best performance)

class Solution:
    
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
               
        def dist(x, y):
            return abs(x[0]- y[0]) + abs(x[1] - y[1])
        
        def calculate(i, visited, cache):
            
            if i == len(workers): return 0
            
            if (i, visited) in cache:
                return cache[(i, visited)]
            
            ans = float('inf')
            for j, bike in enumerate(bikes):
                if visited & 1 << j: continue
                ans = min(ans, dist(bike, workers[i]) + calculate(i+1, visited | 1 << j, cache))
            cache[(i, visited)] = ans
            return ans
        
        return calculate(0, 0, {})
        
# 3. DP with bitmap

class Solution:
    
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        def dist(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        m, n = len(workers), len(bikes)
        dp = [[float('inf')]*(1 << n) for _ in range(m+1)]
        dp[0][0] = 0
        
        for i, worker in enumerate(workers):
            for bitBike in range(1 << n):
                for j, bike in enumerate(bikes):
                    if bitBike & (1 << j) == 0:   # not seen
                        dp[i+1][bitBike | (1 << j)] = min(dp[i+1][bitBike | (1 << j)], dp[i][bitBike] + dist(worker, bike))
        return min(dp[-1])