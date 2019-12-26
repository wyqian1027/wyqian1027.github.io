# 1. O(N^2) DP

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if not nums: return 0
        up = [1]     # max length subsequence end here with peak
        down = [1]   # max length subsequence end here with valley
        maxAns = 1
        
        for i in range(1, len(nums)):
            cur = nums[i]
            maxCount = 0
            for j, count in enumerate(up):
                if cur < nums[j]:
                    maxCount = max(maxCount, count + 1)
            down.append(maxCount)
            maxCount = 0
            for j, count in enumerate(down):
                if cur > nums[j]:
                    maxCount = max(maxCount, count + 1)
            up.append(maxCount)
            maxAns = max(maxAns, max(up[-1], down[-1]))
        
        return maxAns
        
# 2. O(N) Greedy
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
                # down = down
            elif nums[i] < nums[i-1]:
                down = up + 1
                # up = up
        return max(up, down)