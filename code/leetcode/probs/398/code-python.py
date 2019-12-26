class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        
        count = 0
        for i in range(len(self.nums)):
            if target == self.nums[i]:
                count += 1
                if random.random() < 1/count:
                    index = i
        
        return index