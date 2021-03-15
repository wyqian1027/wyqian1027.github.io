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

# Optimized with O(1) space
# compare both ends with two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        left = 0; right = len(height)-1;
        leftMax = rightMax = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    s += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    s += rightMax - height[right]
                right -= 1        
        return s
