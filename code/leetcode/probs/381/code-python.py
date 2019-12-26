import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.d = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.d[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.d[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.d[val]:
            index = self.d[val].pop()
            self.nums[-1], self.nums[index] = self.nums[index], self.nums[-1]
            self.d[self.nums[index]].add(index)
            self.d[self.nums[index]].discard(len(self.nums) - 1)
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if len(self.nums) > 0:
            return random.choice(self.nums)