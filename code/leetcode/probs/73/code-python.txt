class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        col0 = 1 
        
        # setting flags
        for i in range(m):
            if matrix[i][0] == 0: 
                col0 = 0
            for j in range(n):
                if matrix[i][j] == 0: 
                    matrix[i][0] = 0
                    break
        for j in range(1, n):
            for i in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    break
                    
        # setting zeros
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        for i in range(m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        if col0 == 0: 
            for i in range(m):
                matrix[i][0] = 0