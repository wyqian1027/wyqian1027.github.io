class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        if not matrix: return
        
        m, n = len(matrix), len(matrix[0])
        def helper(r, c):
            matrix[r][c], matrix[c][n-1-r], matrix[m-1-r][n-1-c], matrix[m-1-c][r] = \
            matrix[m-1-c][r], matrix[r][c], matrix[c][n-1-r], matrix[m-1-r][n-1-c]
        
        for r in range(m // 2):
            for c in range(r, n - 1 - r):
                helper(r, c)