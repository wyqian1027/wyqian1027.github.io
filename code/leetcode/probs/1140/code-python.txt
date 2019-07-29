# Build look up key for DP Cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        n = len(piles)
        
        def cal(piles, M):
            p = str(len(piles)) + "-" + str(M)
            if p in cache:
                return cache[p]
            tot = sum(piles)
            if len(piles) <= 2*M: return tot
            num = tot
            for x in range(1, 2*M+1):
                num = min(num, cal(piles[x:], max(x, M)))
            ans = tot - num
            cache[p] = ans
            return ans        
        return cal(piles, 1)

# Minmax Solution from li-_-il
def stoneGameII(self, a: List[int]) -> int:
        @lru_cache(maxsize=None)
        def minimax(st, m, player):
            if st >= len(a): return 0
            if player:
                return max([sum(a[st:st+x]) + minimax(st+x, max(m,x), player^1) for x in range(1, 2*m+1)])
            else:
                return min([minimax(st+x, max(m,x), player^1) for x in range(1, 2*m+1)])
        return minimax(0, 1, 1) 