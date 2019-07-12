class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        r, b, g = 0, 0, 0
        for cost in costs:
            newR = min(b, g) + cost[0]
            newB = min(r, g) + cost[1]
            newG = min(r, b) + cost[2]
            r, b, g = newR, newB, newG
        
        return min(r, b, g)