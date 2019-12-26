from collections import defaultdict, deque

class Solution:
    def calcEquation(self, eqns: List[List[str]], vals: List[float], qs: List[List[str]]) -> List[float]:
        
        g = Graph()
        
        for i in range(len(vals)):
            g.add(eqns[i][0], eqns[i][1], vals[i])
            g.add(eqns[i][1], eqns[i][0], 1/vals[i])
        
        res = []
        for fromV, toV in qs:
            res.append(g.getWeightsBetween(fromV, toV))
        
        return res
        
class Graph:
    
    def __init__(self):
        self.d = defaultdict(list)
        
    def add(self, fromV, toV, weight):
        self.d[fromV].append((toV, weight))
        self.d[toV].append((fromV, 1/weight))
        
    def getWeightsBetween(self, fromV, toV):
        
        visited = set()
        
        if fromV not in self.d or toV not in self.d: return -1.0
        if fromV == toV: return 1.0
        
        q = deque(self.d[fromV])

        while q:
            v, wt = q.pop()
            visited.add(v)                
            for nextV, nextWt in self.d[v]:
                if nextV == toV:
                    return wt*nextWt
                if nextV not in visited:
                    q.append((nextV, wt*nextWt))
        
        return -1.0
