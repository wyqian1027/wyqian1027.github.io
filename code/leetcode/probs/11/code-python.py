class Solution:

    def maxArea(self, height: List[int]) -> int:
        
        i, j = 0, len(height) - 1
        area = 0
        
        while i < j:
            h1, h2 = height[i], height[j]
            area = max(area, min(h1, h2)*(j-i))
            if h1 <= h2:
                i += 1
            else:
                j -= 1
                
        return area