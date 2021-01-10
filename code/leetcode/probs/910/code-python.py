class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        
        A.sort()
        ans = float('inf')
        ans = A[-1] - A[0]
        
        for i in range(len(A)-1):
            a = A[i]; b = A[i+1]
            hi = max(a + K, A[-1] - K)
            lo = min(b - K, A[0] + K)
            ans = min(ans, hi - lo)
        
        return ans