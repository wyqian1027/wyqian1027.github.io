# First thought process (col0 is similar)
class Solution:
    def setZeroes(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(A); n = len(A[0]) 

        r0 = 1 # store 0th-row separately
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    if i == 0:
                        r0 = 0
                    else:
                        A[i][0] = 0
                    A[0][j] = 0
        
        # do all rows but 0th
        for i in range(1, m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] = 0
              
        # do all columns
        for i in range(n):
            if A[0][i] == 0:
                for j in range(m):
                    A[j][i] = 0 
        
        # last do row-0th
        if r0 == 0:
            for i in range(n):
                A[0][i] = 0

# Optimization
class Solution:
    def setZeroes(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(A); n = len(A[0])
        c0 = 1 
        for i in range(m):
            if A[i][0] == 0: c0 = 0
            for j in range(1, n):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0
                
        for i in range(m-1, -1, -1):
            for j in range(n-1, 0, -1):
                if A[i][0] == 0 or A[0][j] == 0:
                    A[i][j] = 0
            if c0 == 0: A[i][0] = 0   
