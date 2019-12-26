class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        index = {num: i for i, num in enumerate(A)}
        dp = {}
        
        ans = 0
        for i, num in enumerate(A):
            for j in range(i):
                need = num - A[j]
                k = index.get(need, -1)
                if k != -1 and k < j:
                    dp[(j, i)] = dp.get((k, j), 2) + 1
                    ans = max(ans, dp[(j, i)])
        
        return ans if ans >= 3 else 0