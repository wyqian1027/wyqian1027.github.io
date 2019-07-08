class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.q or timestamp != self.q[-1][0]:
            self.q.append([timestamp, 1])
        else:
            self.q[-1][1] += 1
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.q and self.q[0][0] + 300 <= timestamp:
            time, count = self.q.popleft()
            self.total -= count
        return self.total
