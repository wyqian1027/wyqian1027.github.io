class Solution:
    
    def __init__(self):
        # We need to persist previous read4 results in self.buf4 for future use
        # Therefore, two ptrs are used to record last seen location and end location.
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
        # In this problem, we overrite existing buf each time read is called.
        while tot < n:
            if self.end4 == self.p4:
                self.end4 = read4(self.buf4)
                self.p4 = 0
                if self.end4 == 0: break
            for i in range(self.p4, self.end4):
                if tot < n:
                    buf[tot] = self.buf4[i]
                    tot += 1
                    self.p4 += 1
        return tot        