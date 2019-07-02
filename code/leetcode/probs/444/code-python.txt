class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        indegree = {}
        
        # base on Graph
        for seq in seqs:
            if len(seq) == 1: 
                if seq[0] not in indegree: indegree[seq[0]] = 0
                continue
            for u, v in zip(seq, seq[1:]):
                if u not in indegree: indegree[u] = 0
                if v not in indegree: indegree[v] = 0
                graph[u].append(v)
                indegree[v] += 1
                
        start = [x for x in indegree if indegree[x] == 0]

        index = 0
        
        while start:
            if len(start) > 1: return False
            node = start.pop()
            print(index, node)
            if index >= len(org) or node != org[index]:
                return False
            else:
                index += 1
            
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    start.append(nei)

        return len(indegree) == len(org)  # Base on original sequence