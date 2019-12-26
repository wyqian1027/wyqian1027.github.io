class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.nxt = iterator.next() if iterator.hasNext() else None
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nxt
        
    def next(self):
        """
        :rtype: int
        """
        val = self.nxt
        self.nxt = self.it.next() if self.it.hasNext() else None
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nxt != None