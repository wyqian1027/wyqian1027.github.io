class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) <= 1: return

        def rotateKernel(matrix, r, l):
            if l <= 1: return
            for i in range(l-1): 
                temp = matrix[r+l-1-i][r]
                matrix[r+l-1-i][r] = matrix[r+l-1][r+l-1-i]
                matrix[r+l-1][r+l-1-i] = matrix[r+i][r+l-1]
                matrix[r+i][r+l-1] = matrix[r][r+i]
                matrix[r][r+i] = temp

        for i in range(len(matrix)//2):
            rotateKernel(matrix, i, len(matrix)-2*i)
