class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        n = len(seats)
        
        res = [float('-inf')]
        for i in range(n):
            if seats[i] == 1:
                res.append(i)
        res.append(float('inf'))
        
        max_dist = 0
        
        p1 = 1
        
        for i in range(n):
            if seats[i] == 0:
                max_dist = max(max_dist, min(res[p1] - i, i - res[p1-1]))
            else:
                p1 += 1
        
        return max_dist