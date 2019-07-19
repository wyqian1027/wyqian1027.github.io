# O(N) using two pointers
class Solution(object):
    def minSubArrayLen(self, s, nums):
        minLen = float('inf')
        tot = 0
        l = 0
        for r, num in enumerate(nums):
            tot += num
            while tot >= s:
                minLen = min(minLen, r-l+1)
                tot -= nums[l]
                l += 1
        return minLen if minLen != float('inf') else 0

# O(NlgN) using binary search
from bisect import bisect_right as br
class Solution(object):
    def minSubArrayLen(self, s, nums):
        minLen = float('inf')
        tot = 0
        acc = []
        for i, num in enumerate(nums):
            tot += num
            if tot >= s:
                minLen = min(minLen, i - br(acc, tot - s) + 1)           
            acc.append(tot)
        return minLen if minLen != float('inf') else 0
        
        