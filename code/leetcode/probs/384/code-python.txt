import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.org = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.org[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(0, len(self.nums)-1):
            swapIdx = random.randrange(i, len(self.nums))
            self.nums[swapIdx], self.nums[i] = self.nums[i], self.nums[swapIdx]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()