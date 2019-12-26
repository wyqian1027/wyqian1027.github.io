class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        
        if not grid or len(grid) <= 1: return 0
        
        res = 0
        prev = []
        
        for i in range(len(grid)):
            ones = {index for index, val in enumerate(grid[i]) if val == 1}
            for el in prev:
                c = len(ones & el)
                res += c*(c-1)//2
            prev.append(ones)
        
        return res