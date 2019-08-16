# 1. BFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for i in range(len(M)):
            for j in range(len(M[0])):
                if i != j and M[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        num_circle = 0
        n = len(M)
        visited = [False]*n
        
        for i in range(n):
            if visited[i]: continue
            num_circle += 1
            q = collections.deque([i])
            visited[i] = True
            while q:
                x = q.popleft()
                for nei in graph[x]:
                    if not visited[nei]:
                        q.append(nei)
                        visited[nei] = True
        return num_circle

# 2 Union Find
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        n = len(M)
        parent = list(range(n))
        rank = [0]*n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
    
        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr: return False
            if rank[xr] < rank[yr]:
                xr, yr = yr, xr
            parent[yr] = xr 
            if rank[xr] == rank[yr]:
                rank[xr] += 1
            return True
            
        for i in range(n):
            for j in range(n):
                if i != j and M[i][j] == 1:
                    union(i, j)
        
        return len(set([find(x) for x in range(n)]))