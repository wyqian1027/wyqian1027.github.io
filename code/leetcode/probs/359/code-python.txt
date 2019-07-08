from heapq import heappush, heappop

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st = set()
        self.pq = []

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        while self.pq and self.pq[0][0] + 10 <= timestamp:
            oldtime, oldmessage = heappop(self.pq)
            self.st.remove(oldmessage)
            
        if message not in self.st:
            self.st.add(message)
            heappush(self.pq, (timestamp, message))
            return True
        return False
