# works for flipping lots of ones, scalable
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = right = 0
        longest = 0
        num_zeros = 0
        
        while right < len(nums):
            if nums[right] == 0:
                num_zeros += 1
            while num_zeros > 1:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest
    
# works for flipping one
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = right = 0
        longest = 0
        last_zero = -1
        
        while right < len(nums):
            if nums[right] == 0:
                if last_zero != -1:
                    left = last_zero + 1
                last_zero = right
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest
        
        