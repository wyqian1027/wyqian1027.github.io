from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # if self.minHeap and num >= self.minHeap[0]:
        #     heappush(self.minHeap,  num)
        # else:
        #     heappush(self.maxHeap, -num)
        #
        # Or simply passing num through both heaps and maxHeap size >= minHeap size
    
        heappush(self.minHeap, num)
        heappush(self.maxHeap, -heappop(self.minHeap))
            
        if len(self.minHeap) + 1 < len(self.maxHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
        # if len(self.maxHeap) < len(self.minHeap):
        #     heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2.0
        else:
            return -self.maxHeap[0]