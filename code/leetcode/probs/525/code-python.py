class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        longest = 0
        
        arr = []
        cur = 0
        for num in nums:
            cur = cur + 1 if num == 1 else cur - 1
            arr.append(cur)
        arr = [0] + arr
        
        d = {} 
        for i, el in enumerate(arr):
            if el not in d:
                d[el] = i
            else:
                longest = max(longest, i - d[el])
        
        return longest