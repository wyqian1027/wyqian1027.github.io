class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        preSum = [0]
        for c in nums:
            preSum.append(preSum[-1] + c)
        
        # max_avg = slope of the preSum 
        def getSlope(i, j):
            return (preSum[j] - preSum[i])/(j-i)
    
        max_avg = float('-inf')
        locs = collections.deque()
        
        for i in range(k, len(preSum)):
            # constrain from right, rightmost loc is local optimal candidate
            while len(locs) >= 2 and getSlope(locs[-2], locs[-1]) >= getSlope(locs[-2], i-k):
                locs.pop()
            locs.append(i-k)
            # constrain from left, leftmost loc is local optimal candidate
            while len(locs) >= 2 and getSlope(locs[0], locs[1]) <= getSlope(locs[0], i):
                locs.popleft()
            max_avg = max(max_avg, getSlope(locs[0], i))
        
        return max_avg
        