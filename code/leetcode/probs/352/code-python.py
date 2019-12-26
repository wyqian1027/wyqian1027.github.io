# O(lgN) for addNum
# O(NlgN) for getIntervals

from heapq import heappush, heappop

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = []
        self.st = set()

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val not in self.st:
            self.st.add(val)
            heappush(self.root, [val, val])

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        res = []
        while self.root:
            left, right = heappop(self.root)
            if not res:
                res.append([left, right])
            else:
                if res[-1][1] + 1 >= left:
                    res[-1][1] = max(res[-1][1], right)
                else:
                    res.append([left, right])
        self.root = res
        return self.root   
