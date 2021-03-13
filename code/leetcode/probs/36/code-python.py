class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or len(board) != 9 or len(board[0]) != 9: return False
        '''
        Just use a unique encoding:
        4th row with a 5: R45
        4th col with a 7: C47
        3rd box with a 6: B36
        '''
        seen = set()
        for i in range(9):
            for j in range(9):
                b = (i//3)*3 + j//3
                if board[i][j] != '.':
                    v = board[i][j]
                    c1, c2, c3 = f"R{i}{v}", f"C{j}{v}", f"B{b}{v}"
                    if c1 in seen or c2 in seen or c3 in seen:
                        return False
                    seen.add(c1)
                    seen.add(c2)
                    seen.add(c3)
        return True
