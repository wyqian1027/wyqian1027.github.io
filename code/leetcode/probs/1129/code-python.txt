# Naive implemntation
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        RED = collections.defaultdict(list)
        BLUE = collections.defaultdict(list)
        
        for u, v in red_edges:
            RED[u].append(v)
        
        for u, v in blue_edges:
            BLUE[u].append(v)
        
        def find_shortest(end, start_color):
            q = collections.deque([[0, start_color, 0]])
            visited = set()
            while q:
                node, color, length = q.popleft()
                if node == end:
                    return length
                g = RED if color == 0 else BLUE
                for nei in g[node]:
                    if (node, nei, color) not in visited:
                        q.append([nei, color^1, length+1])
                        visited.add((node, nei, color))
            return float('inf')
        
        res = []
        for i in range(n):
            l = min(find_shortest(i, 0), find_shortest(i, 1))
            res.append(l if l != float('inf') else -1)
        return res
        
# Improved time complexity:
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        RED = collections.defaultdict(list)
        BLUE = collections.defaultdict(list)
        
        for u, v in red_edges:
            RED[u].append(v)
        
        for u, v in blue_edges:
            BLUE[u].append(v)
        
        res = [float('inf')]*n
        
        def find_shortest(start_color):
            q = collections.deque([[0, start_color, 0]])
            visited = set()
            while q:
                node, color, length = q.popleft()
                res[node] = min(res[node], length)
                g = RED if color == 0 else BLUE
                for nei in g[node]:
                    if (nei, color) not in visited:
                        q.append([nei, color^1, length+1])
                        visited.add((nei, color))
        
        find_shortest(0)
        find_shortest(1)
        for i in range(n):
            if res[i] == float('inf'):
                res[i] = -1
        return res