# Naive checking by comparing mid and target values
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            m = lo + (hi - lo) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                if nums[lo] <= nums[m]:
                    lo = m + 1
                elif target >= nums[lo]:
                    hi = m - 1
                else:
                    lo = m + 1
            else:   # nums[m] > target
                if nums[lo] > nums[m]:
                    hi = m - 1
                elif nums[lo] <= target:
                    hi = m - 1
                else:
                    lo = m + 1
        return -1

# (shorter) Better grouping, by comparing lo and mid values first!!!!!        
class Solution    
    def search(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            
            m = lo + (hi - lo) // 2
            
            if nums[m] == target:
                return m
            elif nums[lo] <= nums[m]:
                if nums[lo] <= target <= nums[m]:
                    hi = m - 1
                else:
                    lo = m + 1
            else:
                if nums[m] <= target <= nums[hi]:
                    lo = m + 1
                else:
                    hi = m - 1
        return -1