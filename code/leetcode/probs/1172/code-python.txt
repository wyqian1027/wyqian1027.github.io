from heapq import *

class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.queue = []
        self.available = []  # record freed popAtStack locations
        

    def push(self, val: int) -> None:
        """
        three cases:
        1. have freed spot because of popAtStack
        2. last stack in queue is not full
        3. queue is full
        """
        
        if self.available:
            index = heappop(self.available)
            if index < len(self.queue):
                self.queue[index].append(val)
                return
            else:
                self.available = []
        if self.queue and len(self.queue[-1]) != self.cap:
            self.queue[-1].append(val)
            return
        self.queue.append([val])
        
        
    def cleanUp(self):
        while self.queue and self.queue[-1] == []:
            self.queue.pop()
        
    def pop(self) -> int:
        self.cleanUp()
        if self.queue:
            return self.queue[len(self.queue) - 1].pop()
        return -1
        

    def popAtStack(self, index: int) -> int:
        if index < len(self.queue) and self.queue[index] != []:
            val = self.queue[index].pop()
            heappush(self.available, index)   # only place to add index to heapq
            return val
        return -1
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)