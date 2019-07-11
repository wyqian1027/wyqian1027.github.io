# Using set.pop()
class PhoneDirectory:

    def __init__(self, maxNumbers):
        self.available = set(range(maxNumbers))

    def get(self):
        return self.available.pop() if self.available else -1

    def check(self, number):
        return number in self.available

    def release(self, number):
        self.available.add(number)
        
# Using Queue and Set
class PhoneDirectory:

    def __init__(self, n: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.st = set([i for i in range(n)])
        self.q = [i for i in range(n)]
        

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.q: 
            x = self.q.pop()
            self.st.remove(x)
            return x
        return -1
        

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.st
        

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number not in self.st:
            self.q.append(number)
            self.st.add(number)