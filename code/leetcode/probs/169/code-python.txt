# 1. Hash Table. O(N) Space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct = collections.Counter(nums)
        n = len(nums)
        for k, v in ct.items():
            if v > n // 2: return k
            
# 2. Boyer-Moore Voting Algorithm. O(1) Space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        count = 0
        for num in nums:
            if num == cand:     # 1. checking
                count += 1
            elif count == 0:    # 2. slots available
                cand = num
                count += 1
            else:               # 3. slots NOT available
                count -= 1
        return cand