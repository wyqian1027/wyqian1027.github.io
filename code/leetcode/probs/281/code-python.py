# python iterator with queue

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = collections.deque([(len(v), iter(v)) for v in [v1, v2] if v])

    def next(self):
        """
        :rtype: int
        """
        l, it = self.v.popleft()
        if l > 1:
            self.v.append((l-1, it))
        return next(it)
            

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.v) > 0 