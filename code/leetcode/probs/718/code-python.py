class Solution1:
    def findLength(self, A: List[int], B: List[int]) -> int:
        
        nA, nB = len(A)+1, len(B)+1
        dp = [[0]*nA for _ in range(nB)]

        for i in range(1, nA):
            for j in range(1, nB):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        
        # Alternatively,
        # for i in range(nA-2, -1, -1):
        #     for j in range(nB-2, -1, -1):
        #         if A[i] == B[j]:
        #             dp[i][j] = dp[i+1][j+1] + 1

        return max(max(row) for row in dp)