# using iterator
class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.v = [(len(x), iter(x)) for x in v if len(x) > 0][::-1]

    def next(self):
        """
        :rtype: int
        """
        l, it = self.v.pop()
        if l > 1:
            self.v.append((l-1, it))
        return next(it)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.v) > 0
        
# O(1) space with row, col pointers
class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.row = 0
        self.col = 0
        self.v = v

    def next(self):
        """
        :rtype: int
        """
        val = self.v[self.row][self.col]
        self.col += 1
        self.hasNext()
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.v):
            if self.col < len(self.v[self.row]):
                return True
            self.col = 0
            self.row += 1
        return False
