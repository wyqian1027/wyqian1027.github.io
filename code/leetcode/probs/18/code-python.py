# base on threeSum and DFS
class Solution:

    def fourSum(self, A, target):
        
        res = []
        A.sort()
        self.nSum(4, A, target, [], res)
        return res
        
    def nSum(self, n, A, target, path, res):
        if len(A) < n: return []
        if sum(A[-n:]) < target or sum(A[:n]) > target: return [] 
        if n == 3:
            for i in range(len(A) - 2):
                if i != 0 and A[i] == A[i-1]: continue

                left, right = i + 1, len(A) - 1
                while left < right:
                    s = A[i] + A[left] + A[right]    
                    if s > target:
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        res.append(path + [A[i], A[left], A[right]])
                        while left < right and A[left] == A[left+1]:
                            left += 1
                        while left < right and A[right] == A[right-1]: 
                            right -= 1
                        left += 1
                        right -= 1
        else:
            for i in range(len(A) - n + 1):
                if i != 0 and A[i] == A[i-1]:
                    continue
                self.nSum(n-1, A[i+1:], target - A[i], path + [A[i]], res)

# base on twoSum and recursion
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        
        def twoSum(nums, target):
            if len(nums) < 2 or nums[0] + nums[1] > target or \
            nums[-1] + nums[-2] < target:
                return []
            i, j = 0, len(nums) - 1
            res = []
            while i < j:
                s = nums[i] + nums[j]
                if s == target:
                    res.append([nums[i], nums[j]])
                    while i+1 < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j-1 and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                            
                elif s > target:
                    j -= 1
                else:
                    i += 1
            return res
        
        def nSum(nums, target, n):
            if len(nums) < n or sum(nums[:n]) > target or \
            sum(nums[-n:]) < target:
                return []
            res = []
            if n == 2:
                return twoSum(nums, target)
            else:
                for i in range(len(nums)-n+1):
                    if i != 0 and nums[i] == nums[i-1]: continue
                    subs = nSum(nums[i+1:], target-nums[i], n-1)
                    for sub in subs:
                        res.append([nums[i]] + sub)
            return res

        return nSum(nums, target, 4)
                    
                
        
        
        

       
