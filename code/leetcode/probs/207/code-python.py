#1. BFS topological sort

class Solution:
    def canFinish(self, n: int, pres: List[List[int]]) -> bool:

        #graph: pre -> course
        graph = collections.defaultdict(list)
        indegrees = [0]*n
        for crs, pre in pres:
            graph[pre].append(crs)
            indegrees[crs] += 1
        
        zeros = collections.deque([crs for crs in range(n) if indegrees[crs] == 0])
        ans = []
        
        while zeros:
            crs = zeros.pop()
            ans.append(crs)
            
            for nxt in graph[crs]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    zeros.append(nxt)
        
        return len(ans) == n

#2. DFS with colors

class Solution:
    def canFinish(self, n: int, pres: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for crs, preq in pres:
            graph[crs].append(preq)
        
        def dfs(u, color):
            color[u] = "GRAY"
            for v in graph[u]:
                if color[v] == "GRAY":
                    return True
                if color[v] == "WHITE" and dfs(v, color) == True:
                    return True
            color[u] = "BLACK"
            return False       
        
        color = ["WHITE"]*n
        for i in range(n):
            if color[i] == "WHITE":
                if dfs(i, color) == True:
                    return False
        return True