#1. DFS recursion, checking node versus intended color
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        def dfs(node, c):
            if node not in colors:
                colors[node] = c
                for nei in graph[node]:
                    if dfs(nei, c ^ 1) == False:
                        return False
            elif colors[node] != c:
                return False
            return True
        
        for node in range(len(graph)):
            if node not in colors:
                if dfs(node, 0) == False:
                    return False
        return True
                
#2. Iterative Approach with Stack or Queue
class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        def check(node):
            if node not in colors:
                stack = [node]
                colors[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in colors:
                            colors[nei] = colors[node] ^ 1
                            stack.append(nei)
                        elif colors[nei] == colors[node]:
                            return False
            return True
        
        return all(check(i) for i in range(len(graph)))