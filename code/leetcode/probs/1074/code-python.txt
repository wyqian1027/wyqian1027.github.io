class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1]
        ans = 0
        for i in range(n):
            for j in range(i, n):
                cur = 0       # current submatrix sum
                d = {0: 1}    # hashtable for frequency of submatrix sum in these two columns
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                    ans += d.get(cur - target, 0)
                    d[cur] = d.get(cur, 0) + 1
        return ans