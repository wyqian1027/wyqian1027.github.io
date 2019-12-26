class Solution:
    
    def __init__(self):
        self.end4 = 0
        self.p4 = 0
        self.buf4 = ["", "", "", ""]
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        tot = 0
        # I thought we would not like override existing buf... but okay
        while tot < n:
            if self.end4 == self.p4:
                self.end4 = read4(self.buf4)
                self.p4 = 0
            if self.end4 == 0: break
            for _ in range(self.p4, self.end4):
                if tot + 1 <= n:
                    buf[tot] = self.buf4[self.p4]
                    tot += 1
                    self.p4 += 1
        return tot        