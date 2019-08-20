class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        
        max_line = 0
        if not M: return 0
        
        m, n = len(M), len(M[0])
        
        h_dp = [[0]* n for _ in range(m)]
        v_dp = [[0]* n for _ in range(m)]
        d_dp = [[0]* n for _ in range(m)]
        a_dp = [[0]* n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if M[r][c] == 0: continue
                v_dp[r][c] = 1 if r == 0 else v_dp[r-1][c] + 1
                h_dp[r][c] = 1 if c == 0 else h_dp[r][c-1] + 1
                d_dp[r][c] = 1 if r == 0 or c == 0 else d_dp[r-1][c-1] + 1
                a_dp[r][c] = 1 if r == 0 or c == n-1 else a_dp[r-1][c+1] + 1
                max_line = max(max_line, h_dp[r][c], v_dp[r][c], d_dp[r][c], a_dp[r][c])
        return max_line