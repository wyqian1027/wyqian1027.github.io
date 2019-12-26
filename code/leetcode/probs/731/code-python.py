# 1. Using Heap (slow), O(NlogN)
from bisect import bisect_left as bl
from heapq import heappush, heappop

class MyCalendarTwo:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        cur = [start, end]
        pq = []
        overlap = 0
        self.add(cur)
        for booking in self.bookings:
            while pq and pq[0] <= booking[0]:
                heappop(pq)
                overlap -= 1
            if overlap >= 2: 
                self.remove(cur)
                return False
            overlap += 1
            heappush(pq, booking[1])
        return True
        
    def add(self, cur):
        self.bookings.insert(bl(self.bookings, cur), cur)
    
    def remove(self, cur):
        self.bookings.remove(cur)
        
# 2.Using two arrays, one for storing overlaps. O(N)         
class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True