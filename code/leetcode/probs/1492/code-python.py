class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        if k > n: return -1
        factors = []
        # O(sqrt(n))
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                factor = i
                k -= 1
                factors.append(factor)
                if k == 0: return factor
                
        # skip if the last factor is a duplicate
        if factors[-1]*factors[-1] == n:
            k += 1
        return n // factors[-k] if k <= len(factors) else -1