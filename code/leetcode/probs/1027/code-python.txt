class Solution:
    def longestArithSeqLength(self, A):

        if len(A) <= 2: return len(A)
        longest = 2
        
        dp = {}
        for i in range(1, len(A)):   # current
            for j in range(i):       # before
                diff = A[j] - A[i]
                if (j, diff) in dp:
                    dp[(i, diff)] = dp[(j, diff)] + 1
                    longest = max(longest, dp[(i, diff)])
                else:
                    dp[(i, diff)] = 2
        return longest