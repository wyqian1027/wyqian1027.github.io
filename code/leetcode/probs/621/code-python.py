# O(NlogN) PriorityQueue + Queue Solution
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # maxheap to pop most time-consuming task
        h = []

        # time order queue for tracking availablity
        # acting like an intermediate ground before pushing to heapq
        times = collections.deque()   
        
        for ch, val in collections.Counter(tasks).items():
            heappush(h, [-val, ch])
        
        time = 0
        res = []
        
        while h or times:
            
            if h:
                v, task = heappop(h)
                if v + 1 < 0:
                    times.append([time, v+1, task])
            else:
                task = "idle"   
                
            # res.append(task)
            
            time += 1
            
            if times and time > times[0][0] + n:
                _, v, task = times.popleft()
                heappush(h, [v, task])
            
        return time

# O(N) special solution
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)
        total = len(tasks)
        valids = {k: 0 for k in counts}
        
        def helper(pos): # find the valid key with the largest count
            ans = "idle", 0
            for task in counts:
                if counts[task] > ans[1] and pos >= valids[task]:
                    ans = task, counts[task]
            return ans[0]
        
        pos = 0
        while total > 0:
            task = helper(pos)
            if task != "idle":
                total -= 1
                counts[task] -= 1
                if counts[task] == 0:
                    del counts[task]
                valids[task] = pos + n + 1
            pos += 1
        
        return pos

