# Best approach is to use Binary Search.

import bisect
class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        bisect.insort(self.events, (start, 1))       # search && insert
        bisect.insort(self.events, (end, -1))

        res = 0
        booking = 0
        for _, state in self.events:
            booking += state
            res = max(res, booking)
        return res