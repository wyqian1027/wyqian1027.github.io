# Extending from II
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = right = 0
        res = 0
        ones = 0
        
        while right < len(A):
            if A[right] == 1:
                ones += 1
            if right - left + 1 - ones > K:
                if A[left] == 1:
                    ones -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        
        return res

# Alternative thinking of zeros
class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        if not A: return 0
        zeros = []
        maxSofar = 0
        for i, num in enumerate(A):
            if num == 0: zeros.append(i)
        
        if len(zeros) <= k: return len(A)
        if k != 0: maxSofar = zeros[k-1]+1
        
        for i in range(k, len(zeros)):
            if i+1 < len(zeros):
                upper = zeros[i+1]
            else:
                upper = len(A)
            lower = zeros[i-k]
            maxSofar = max(maxSofar, upper - lower - 1)
        return maxSofar