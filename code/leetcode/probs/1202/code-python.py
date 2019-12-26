
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        s = list(s)
        
        def sort_string_by_indices(indices):
            substring = []
            indices.sort()
            for index in indices:
                substring.append(s[index])
            substring.sort()
            for i, index in enumerate(indices):
                s[index] = substring[i]

        graph = collections.defaultdict(list)
        
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        for i in range(len(s)):
            if i in visited or i not in graph: continue
            q = collections.deque([i])
            indices = []
            visited.add(i)
            while q:
                cur = q.popleft()
                indices.append(cur)
                for nei in graph[cur]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            sort_string_by_indices(indices)
        
        return "".join(s)