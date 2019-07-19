class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {0: -1}
        s = 0
        maxLen = 0
        for i, num in enumerate(nums):
            s += num
            if s - k in d:
                maxLen = max(maxLen, i - d[s-k])
            if s not in d:
                d[s] = i
        return maxLen