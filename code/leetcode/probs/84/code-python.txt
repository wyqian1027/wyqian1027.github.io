# Optimal solution with Stack

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
    
        stack = []
        ans = 0
        heights.append(0) # for final pops
        
        for i, curH in enumerate(heights):
            while stack and heights[stack[-1]] > curH:
                popH = heights[stack.pop()]
                left = stack[-1] if stack else -1
                ans = max(ans, (i - left - 1) * popH)
            # print(i, stack, ans)
            stack.append(i)
        
        heights.pop()
        return ans