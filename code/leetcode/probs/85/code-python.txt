class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return 0
    
        heights = [0 for _ in range(len(matrix[0]))] + [0]
        
        ans = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            stack = []
            for k in range(len(heights)):
                curH = heights[k]
                while stack and heights[stack[-1]] > curH:
                    popH = heights[stack.pop()]
                    left = -1 if not stack else stack[-1]
                    ans = max(ans, (k - left - 1)*popH)
                stack.append(k)
        
        return ans