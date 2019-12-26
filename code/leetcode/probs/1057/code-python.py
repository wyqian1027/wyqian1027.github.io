# 1. Using Heap
# complexity:
# O(WB) + O(W(BlgB)) + O(WlgW) + O(WBlgW) -> O(WBlgWB) 


from heapq import heappush, heappop, heapify

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        s = []
        def dist(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        for i, worker in enumerate(workers):
            s.append([])
            for j, bike in enumerate(bikes):
                s[-1].append([dist(worker, bike), i, j])
            s[-1].sort(reverse=True)
        
        h = [x.pop() for x in s]
        heapq.heapify(h)
                
        ans = [-1]*len(workers)
        seenBike = set()
        
        while len(seenBike) != len(workers):
            _, workerInd, bikeInd = heappop(h)
            if bikeInd in seenBike:
                heappush(h, s[workerInd].pop())
            else:
                ans[workerInd] = bikeInd
                seenBike.add(bikeInd)
        
        return ans
        
# 2. Using Distance Map, since maxDistance is 2000
# complexity: O(2000WB) -> O(WB)

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        distMap = collections.defaultdict(list)
        def dist(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distMap[dist(worker, bike)].append([i, j])

        seenBike = set()
        ans = [None]*len(workers)
        n = 0
        
        for cost in sorted(distMap.keys()):
            for i, j in distMap[cost]:
                if ans[i] == None and j not in seenBike:
                    ans[i] = j
                    seenBike.add(j)
                    n += 1
                    if n == len(workers): break
                    
        return ans
            