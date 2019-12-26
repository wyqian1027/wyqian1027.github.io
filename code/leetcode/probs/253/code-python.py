# 1. Using Heap
from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, A: List[List[int]]) -> int:
        A.sort()
        h = []
        for l, r in A:
            if h and h[0] <= l:
                heappop(h)
            heappush(h, r)
        return len(h)
  
# 2. Using two pointers
# If start < end, meaning we need to find a room, either use available room (available -= 1) or ask for a new room (numRooms += 1)
# If start >= end, we finished a meeting, free up one room (available += 1)
# Basically think of end point as resources, while traverse on start point.

class Solution:
    def minMeetingRooms(self, A: List[List[int]]) -> int:
        if not A or len(A) == 0: return 0
        starts = sorted([x[0] for x in A])
        ends   = sorted([x[1] for x in A])
        i = j = 0
        numRooms = available = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                i += 1
            else:
                available += 1
                j += 1
        return numRooms