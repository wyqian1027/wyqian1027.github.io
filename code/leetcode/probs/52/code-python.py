class Solution:
    def totalNQueens(self, n: int) -> int:      
        self.res = 0
        # using the strategy of restriction
        BX = [False]*2*n # backward lines 0->n-1->2n-1
        FX = [False]*2*n # forward lines  0->n-1->2n-1
        V = [False]*n  # vertical lines 0->n-1
        
        def getBXIndex(r, c):
            return n + r - c
        
        def getFXIndex(r, c):
            return n + (n-1-c) - r
        
        def dfs(r):
            if r >= n:
                self.res += 1
                return
            for c in range(n):
                bi = getBXIndex(r, c)
                fi = getFXIndex(r, c)
                if not (V[c] or BX[bi] or FX[fi]):
                    V[c] = BX[bi] = FX[fi] = True
                    dfs(r+1)
                    V[c] = BX[bi] = FX[fi] = False
        dfs(0)
        return self.res
