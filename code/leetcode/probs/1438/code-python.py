from heapq import heappush, heappop

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxVals = []
        minVals = []
        ans = 1
        index = 0
        
        for i, num in enumerate(nums):
            heappush(maxVals, [-num, i])
            heappush(minVals, [num, i])
            while -maxVals[0][0] - minVals[0][0] > limit:
                index = min(maxVals[0][1], minVals[0][1]) + 1
                while maxVals[0][1] < index: heappop(maxVals)
                while minVals[0][1] < index: heappop(minVals)
            ans = max(ans, i - index + 1)
        return ans

        