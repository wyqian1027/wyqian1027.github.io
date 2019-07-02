# 1. BFS Topological Sorting

class Solution:
    
    def findOrder(self, n: int, preq: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        indegree = [0]*n
        for toV, fromV in preq:
            graph[fromV].append(toV)
            indegree[toV] += 1
        
        start = [x for x in range(n) if indegree[x] == 0]
        q = collections.deque(start)
        res = []
        
        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == n else []

# 2. DFS with colors + flag

class Solution:
    
    def findOrder(self, n: int, preq: List[List[int]]) -> List[int]:
        
        self.graph = collections.defaultdict(list)
        for v, u in preq:
            self.graph[u].append(v)
            
        visited = [0]*n
        stack = []
        self.flag = True
        
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, stack, visited)
        return stack if len(stack) == n else []
    
    def dfs(self, node, stack, visited):
        if not self.flag: return
        visited[node] = 1
        for nei in self.graph[node]:
            if visited[nei] == 0:
                self.dfs(nei, stack, visited)
            if visited[nei] == 1:
                self.flag = False
                return
        visited[node] = 2
        stack.insert(0, node)