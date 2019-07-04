import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}  # map num to index
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.d[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        
        index = self.d[val]
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.d[self.nums[index]] = index
        self.nums.pop()
        del self.d[val]
        return True
     

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.nums: return random.choice(self.nums)