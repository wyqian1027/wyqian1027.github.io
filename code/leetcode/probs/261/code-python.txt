class Solution1:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n == 1 and edges == []: return True
        
        graph = collections.defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        for u in graph:
            if len(graph[u]) == 0: return False
            
        visited = [0] * n
        
        def hasCycle(x, visited, parent):
            
            visited[x] = 1
            
            for nei in graph[x]:
                
                #Visited and Not Parents => Cycle
                if (visited[nei] == 1 and nei != parent):
                    
                    return True
                
                #not visited: call again and found cycle => Cycle
                if (visited[nei] == 0 and hasCycle(nei, visited, x)):
                    
                    return True
            
            return False
                
        
        if hasCycle(0, visited, -1):
            
            return False
        
        return all(visited)


class Solution2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        parents = list(range(n))
        ranks = [0]*n
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        for x, y in edges:
            xr, yr = find(x), find(y)
            if xr == yr: return False
            if ranks[xr] < ranks[yr]:
                xr, yr = yr, xr
            parents[yr] = xr
            if ranks[xr] == ranks[yr]: ranks[xr] += 1
        
        return len({find(i) for i in range(n)}) == 1
                       
        
        