class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        if not costs: return 0
        k = len(costs[0])
        prevColor, prevMin, prevMin2 = -1, 0, 0
        
        for cost in costs:
            curColor, curMin, curMin2 = -1, float('inf'), float('inf')
            for c, p in enumerate(cost):
                s = prevMin2 if c == prevColor else prevMin
                s += p
                if s < curMin:
                    curMin2 = curMin
                    curMin = s
                    curColor = c
                elif curMin <= s < curMin2:
                    curMin2 = s
            prevColor, prevMin, prevMin2 = curColor, curMin, curMin2
        return curMin