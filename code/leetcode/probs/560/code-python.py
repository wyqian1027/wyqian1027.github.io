class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        acc = 0
        d = {0: 1}
        res = 0
        for num in nums:
            acc += num
            if acc - k in d:
                res += d[acc - k]
            d[acc] = d.get(acc, 0) + 1
        
        return res