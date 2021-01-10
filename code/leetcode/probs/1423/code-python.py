# from functools import lru_cache

class Solution:
    def maxScore(self, points: List[int], k: int) -> int:
        
#         cache = {}
#         @lru_cache(None)
#         def getMaxScore(i, j, k):
#             if i > j or k == 0: return 0
#             # if (i, j, k) in cache: return cache[(i, j, k)]
#             ans = max(points[i] + getMaxScore(i+1, j, k-1), \
#                       points[j] + getMaxScore(i, j-1, k-1))
#             # cache[(i, j, k)] = ans
#             return ans
#         return getMaxScore(0, len(points)-1, k)

        curSum = 0
        minSum = float('inf')
        m = len(points) - k # m = length of the leftover subarray
        for i, p in enumerate(points):
            curSum += p
            if i >= m: 
                curSum -= points[i-m]
            if i >= m-1:
                minSum = min(minSum, curSum)
        
        return sum(points) - minSum