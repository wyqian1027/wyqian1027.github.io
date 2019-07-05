class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]
        graph = collections.defaultdict(list)
        degrees = [0]*n
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
            graph[u].append(v)
            graph[v].append(u)
        
        leaves = [x for x in range(n) if degrees[x] == 1]
        
        q = collections.deque(leaves)
        while q:
            last, size = list(q), len(q)
            for _ in range(size):
                node = q.popleft()
                for nei in graph[node]:
                    if degrees[nei] > 0:
                        degrees[node] -= 1
                        degrees[nei] -= 1
                        if degrees[nei] == 1:
                            q.append(nei)
        return last