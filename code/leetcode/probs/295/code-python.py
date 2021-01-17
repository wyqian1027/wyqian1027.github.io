from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []  # Upper bucket
        self.maxHeap = []  # Lower bucket       

    def addNum(self, num: int) -> None:
        # Pass new number through BOTH bucket!
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        # Make it evenly distributed
        if len(self.minHeap) - len(self.maxHeap) > 1:
            e = heappop(self.minHeap)
            heappush(self.maxHeap, -e)
        

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 1:
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Follow up:
# 1. Use an integer array of size 100 to store the frequency and we can find the median by 
# accumulating the sum, O(100) = O(1)
# 2. Use an Hashmap for occurance outside this range of 100.