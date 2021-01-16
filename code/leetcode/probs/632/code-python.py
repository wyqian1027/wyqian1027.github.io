from heapq import heappop, heappush, heapify

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        # priority queue of left-end points, and their positions
        pq = [[row[0], i, 0] for i, row in enumerate(nums)]
        heapify(pq)
        ans = float("-inf"), float("inf")
        
        right = max(row[0] for row in nums)
        while pq:
            # get the smallest left element
            left, i, j = heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                return ans
            nxt = nums[i][j+1]
            # keep the right end-point increasing
            right = max(right, nxt)
            heappush(pq, [nxt, i, j+1])
        
        return ans