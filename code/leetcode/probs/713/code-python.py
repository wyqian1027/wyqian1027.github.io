# O(N) sliding window
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0 # must take care 1 otherwise pain
        cur = 1
        left = 0
        total = 0
        for right, val in enumerate(nums):
            cur = cur*val
            while cur >= k:
                cur //= nums[left]
                left += 1
            total += right - left + 1
        return total

# O(NlgN) convert to subarraySum, with binary search to find pivot pos
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        k = math.log(k)
        prefix = [0]
        for num in nums:
            prefix.append(math.log(num) + prefix[-1])
        ans = 0
        for i, a in enumerate(prefix):
            pos = bisect.bisect_left(prefix, a-k+1e-9, 0, i)
            ans += i - pos
            # checking sum afterwards
            # pos = bisect.bisect(prefix, a+k-1e-9, i+1)
            # ans += pos - i - 1
        return ans
