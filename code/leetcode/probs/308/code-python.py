# O(N) solution
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]
        self.m = matrix

    def update(self, row: int, col: int, val: int) -> None:
        original = self.m[row][col]
        if col != 0: original -= self.m[row][col-1]
        diff = val - original
        for j in range(col, len(self.m[0])):
            self.m[row][j] += diff
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            res += self.m[i][col2]
            if col1 != 0: res -= self.m[i][col1-1]
        return res
        
# 2D Binary Index Tree
# Original post see https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/75900/Python-2D-binary-indexed-tree
class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix: return
        self.M, self.N = len(matrix), len(matrix[0])
        self.mat  = [[0] * self.N for _ in range(self.M)]
        self.BIT  = [[0] * (self.N + 1) for _ in range(self.M + 1)]
        for i in range(self.M):
            for j in range(self.N):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        diff  = val - self.mat[row][col]
        i, self.mat[row][col] = row + 1, val
        while i <= self.M:
            j = col + 1
            while j <= self.N:
                self.BIT[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def sumRegion(self, row1, col1, row2, col2):
        return self.getsum(row2, col2)         + \
               self.getsum(row1 - 1, col1 - 1) - \
               self.getsum(row1 - 1, col2)     - \
               self.getsum(row2, col1 - 1)

    def getsum(self, row, col):
        res, i = 0, row + 1
        while i:
            j = col + 1
            while j:
                res += self.BIT[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res