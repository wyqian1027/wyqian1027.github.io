# O(1) Time really neat solution, no need for board!
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.D = 0
        self.antiD = 0
        self.row = [0]*n
        self.col = [0]*n
        self.size = n
        
    def move(self, r: int, c: int, player) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        add = 1 if player == 1 else -1
        if r == c: self.D += add
        if r + c == self.size - 1: self.antiD += add
        self.row[r] += add
        self.col[c] += add
        if (abs(self.D) == self.size or abs(self.antiD) == self.size or \
            abs(self.row[r]) == self.size or abs(self.col[c]) == self.size):
            return player
        return 0