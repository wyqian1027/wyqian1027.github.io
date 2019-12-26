class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.total = 0
        self.size = size
        self.stream = collections.deque()
    

    def next(self, val: int) -> float:
        self.total += val
        self.stream.append(val)
        if len(self.stream) > self.size:
            self.total -= self.stream.popleft()
        return self.total / len(self.stream)
