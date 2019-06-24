# 1. DFS, O(N^N)
class Solution:
   
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for u, v, w in times:
            graph[u].append([v, w])
        
        delays = [float('inf') for _ in range(N+1)]
        
        def dfs(node, cost):
            if delays[node] <= cost: return
            delays[node] = cost
            for v, w in graph[node]:
                dfs(v, cost + w)
        
        dfs(K, 0)
        maxDelay = max(delays[1:])
        
        return maxDelay if maxDelay != float('inf') else -1
        
# 2. Dijkstra with PriorityQueue O(NlogN)
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])
            
        pq = [(0, K)]
        delays = {}
        
        while pq:
            cost, node = heapq.heappop(pq)
            if node in delays: continue
            delays[node] = cost
            for v, w in graph[node]:
                if v not in delays:
                    heapq.heappush(pq, (w + cost, v))

        return -1 if len(delays) < N else max(delays.values())
        
# 3. Dijkstra with Set O(N^2)
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])
            
        delays =[float('inf') for _ in range(N+1)]
        delays[K] = 0
        seen = set()
        
        while True:
            cand = -1
            cost = float('inf')
            for i in range(1, N+1):
                if i not in seen and delays[i] < cost:
                    cand = i
                    cost = delays[i]
            if cand == -1: break
            seen.add(cand)
            
            for v, w in graph[cand]:
                delays[v] = min(delays[v], w + cost)
                
        return -1 if len(seen) < N else max(delays[1:])