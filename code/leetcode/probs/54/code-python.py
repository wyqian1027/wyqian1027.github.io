class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]: return []
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(matrix), len(matrix[0])
        upper, lower, left, right = 0, m-1, 0, n-1  # box window limit
        d = 0
        r = c = 0
        res = []
        
        for _ in range(m*n):
            res.append(matrix[r][c])
            if not (upper <= r + dirs[d][0] <= lower and left <= c + dirs[d][1] <= right):
                if d == 0: upper += 1
                elif d == 1: right -= 1
                elif d == 2: lower -= 1
                else: left += 1
                d = (d + 1) % 4
            r += dirs[d][0]
            c += dirs[d][1]
            
        return res
