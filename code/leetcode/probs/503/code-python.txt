class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        n = len(nums)
        ans = [-1]*n
        
        for i in range(n*2):
            cur = nums[i % n]
            while stack and nums[stack[-1]] < cur:
                ans[stack.pop()] = cur
            stack.append(i % n)
        return ans