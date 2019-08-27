class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if not nums: return []
        
        nums.sort()
        
        dp = [0]*len(nums)     # store size of maximal subset formed by nums[i] as the largest element
        prev = [-1]*len(nums)  # store location of previous element
        largest = 0 
        largest_loc = 0
        
        for i in range(len(nums)):
            
            dp[i] = 1
            
            for j in range(i):
                
                if nums[i] % nums[j] == 0:
                    
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
                        if dp[i] > largest:
                            largest = dp[i]
                            largest_loc = i
                            
        loc = largest_loc
        res = []
        
        while loc != -1:
            res.append(nums[loc])
            loc = prev[loc]
        
        return res