class Solution:
    
    def trap(self, height: List[int]) -> int:
        
        leftH, rightH = [0]*len(height), [0]*len(height)
        
        seen = 0
        for i in range(len(height)):
            seen = max(seen, height[i])
            leftH[i] = seen
            
        seen = 0
        for i in reversed(range(len(height))):
            seen = max(seen, height[i])
            rightH[i] = seen
            
        ans = 0
        for i in range(len(height)):
            ans += min(leftH[i], rightH[i]) - height[i]
        
        return ans