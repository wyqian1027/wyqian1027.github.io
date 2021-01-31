class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        acc = res = 0
        d = {0: 1}
        for num in nums:
            acc += num
            res += d.get(acc - k, 0)
            d[acc] = d.get(acc, 0) + 1
        return res