class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]: return False
        
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        
        m, n = len(matrix), len(matrix[0])
        
        lo, hi = 0, m*n-1
        
        while lo <= hi:
            mid = (lo + hi) // 2;
            r, c = divmod(mid, n)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False
        