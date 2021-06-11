class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        n = len(graph); cost = 0; target = (1 << n) - 1
        # for each path: (bitmask, cur_node)
        q = [(1 << i, i) for i in range(n)]
        visited = set()
        
        while q:
            tmp = []
            for mask, cur in q:
                # Note: return the cost when mask matched, as the cost oof any path 
                # on this BFS layer is the same for this problem
                if mask == target:
                    return cost
                for nei in graph[cur]:
                    new_mask = (1 << nei) | mask
                    if (new_mask, nei) not in visited:
                        tmp.append((new_mask, nei))
                        visited.add((new_mask, nei))
            q = tmp
            cost += 1
            
        return -1