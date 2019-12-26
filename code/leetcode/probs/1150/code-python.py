class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        left, right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        return right - left > len(nums) // 2

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        def search(A, x):           # find left end point of insertion
            lo, hi = 0, len(A)      # Important: len(A) is necessary to mimic bisect_right
            while lo < hi:
                m = lo + (hi - lo) // 2
                if A[m] < x:
                    lo = m + 1
                else:
                    hi = m
            return lo
        
        if not nums: return False
        
        left, right = search(nums, target), search(nums, target+1)

        return right - left > len(nums) // 2