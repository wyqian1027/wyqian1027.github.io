from functools import lru_cache
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        # Euclidean algo
        def gcd(x, y):
            return y if x == 0 else gcd(y % x, x)
        
        @lru_cache(None)
        def lcm(x, y):
            return x*y//gcd(x, y)
        
        def count(n, a, b, c):
            s =  n // a + n // b + n // c
            s -= n // lcm(a, b) + n // lcm(a, c) + n // lcm(b, c)
            s += n // lcm(lcm(a, b), c)
            return s
        
        l, r = 1, 2*10**9
        while l < r:
            m = l + (r - l) // 2
            if count(m, a, b, c) < n:
                l = m + 1
            else:
                r = m
        return l