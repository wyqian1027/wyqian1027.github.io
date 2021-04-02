class Solution:
    def grayCode(self, n: int) -> List[int]:
        cache = {1: [0, 1]}        
        def helper(n):
            if n in cache: return cache[n]
            cache[n] = helper(n-1) + [(1<<(n-1)) + x for x in helper(n-1)][::-1]
            return cache[n]
        return helper(n)

class Solution:
    def grayCode(self, n: int) -> List[int]:
        total = 1 << n
        res = [0]
        shift = 1
        while len(res) != total:
            res += [x + shift for x in res[::-1]] 
            shift *= 2
        return res
