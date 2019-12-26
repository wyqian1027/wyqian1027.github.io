import collections

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        
        forbidden = collections.defaultdict(set)
        
        
        res = []
        for garden in range(1, N+1):
            for color in range(1, 5):
                if color not in forbidden[garden]:
                    this_color = color
                    res.append(this_color)
                    break
            for nei in graph[garden]:
                forbidden[nei].add(this_color)
        
        return res