class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []
        

    def push(self, x: int) -> None:
        if self.isEmpty():
            self.mins.append(x)
        else:
            self.mins.append(min(self.mins[-1], x))
        self.stack.append(x)


    def pop(self) -> None:
        if not self.isEmpty():
            self.mins.pop()
            self.stack.pop()          
        

    def top(self) -> int:
        if not self.isEmpty():
            return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.isEmpty():
            return self.mins[-1]    
        
    def isEmpty(self):
        if not self.stack: return True
        return False