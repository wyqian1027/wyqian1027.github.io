class Solution:
    
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
            
        self.board = board
        self.state = {str(x): 0 for x in range(1, 10)}
        self.initState()
        self.solve()

    def initState(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != ".":
                    self.state[self.board[row][col]] += 1
    
    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1
    
    def solve(self):
        row, col = self.findUnassigned()
        #no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True
               
        for num in set([x for x in self.state if self.state[x] != 9]):
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                self.state[num] += 1
                if self.solve():
                    return True
                self.board[row][col] = "."
                self.state[num] -= 1
        return False
            
    def isSafe(self, row, col, ch):
        boxrow = row - row%3
        boxcol = col - col%3
        if self.checkrow(row,ch) and self.checkcol(col,ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False
    
    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True
    
    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True
       
    def checksquare(self, row, col, ch):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] == ch:
                    return False
        return True
        