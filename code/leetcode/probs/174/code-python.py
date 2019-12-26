class Solution:
    def calculateMinimumHP(self, dungeon):
        
        rowN, colN = len(dungeon), len(dungeon[0])
        cache = {}
        
        def calculate(r, c):
            
            if (r, c) in cache: return cache[(r,c)]
            
            if r == rowN - 1 and c == colN - 1:
                cache[(r, c)] = max(1, 1 - dungeon[r][c])
            elif c == colN - 1:
                cache[(r, c)] = max(1, calculate(r+1, c) - dungeon[r][c])
            elif r == rowN - 1:
                cache[(r, c)] = max(1, calculate(r, c + 1) - dungeon[r][c])
            else:
                cache[(r, c)] = max(1, min(calculate(r+1, c), calculate(r, c+1)) - dungeon[r][c])
            
            return cache[(r, c)]
        
        return calculate(0, 0)