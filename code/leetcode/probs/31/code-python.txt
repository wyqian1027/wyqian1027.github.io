class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        found = False
        
        for i in range(len(nums)-1, -1, -1):
            
            if i == len(nums) - 1 or nums[i] >= nums[i+1]:
                continue
            else:
                nextVal, nextLoc = float('inf'), -1
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i] and nums[j] <= nextVal:
                        nextVal = nums[j]
                        nextLoc = j
                nums[i], nums[nextLoc] = nextVal, nums[i]
                self.reverse(nums, i+1, len(nums)-1)
                found = True
                break

        if not found: self.reverse(nums, 0, len(nums)-1)
            
            
    def reverse(self, nums, i, j):
                 
        while (i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1