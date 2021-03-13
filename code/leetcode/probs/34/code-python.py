class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        lo = 0; hi = len(nums)-1;
        ans = [-1, -1]
        
        # find leftmost   
        while lo < hi:
            m = lo + (hi-lo)//2
            if target <= nums[m]:
                hi = m
            else:
                lo = m + 1
                
        if nums[lo] != target: return ans
        
        # find rightmost
        ans[0] = lo; hi = len(nums)-1
        while lo < hi:
            m = lo + (hi-lo+1)//2
            if target >= nums[m]:
                lo = m
            else:
                hi = m - 1
        ans[1] = hi
        
        return ans
