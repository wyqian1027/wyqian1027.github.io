# Naive Backtracking
class Solution:
    
    def numTilePossibilities(self, tiles: str) -> int:
        
        tiles = sorted(list(tiles))
        taken = [False]*len(tiles)
        res = set()
        
        def dfs(tiles, taken, path):
            res.add(path)
            for i in range(len(tiles)):
                if not taken[i]:
                    taken[i] = True
                    dfs(tiles, taken, path + tiles[i])
                    taken[i] = False
        dfs(tiles, taken, "")
        return len(res) - 1
        
# Backtracking with Dictionary
class Solution:
    def numTilePossibilities(self, A: str) -> int:
        
        self.st = set()
        ct = collections.Counter(A)
        self.dfs("", ct)
        return len(self.st)
    
    def dfs(self, path, ct):
           
        if path: self.st.add(path)
        for k, v in ct.items():
            if v > 0:
                ct[k] -= 1
                self.dfs(path+k, ct)
                ct[k] += 1