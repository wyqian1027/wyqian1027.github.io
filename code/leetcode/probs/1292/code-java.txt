class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        
        int m = mat.length, n = mat[0].length;
        int[][] dp = new int[m+1][n+1];
        
        for (int i = 1; i < m+1; i++){
            for (int j = 1; j < n+1; j++){
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1];
            }
        }
        
        int maxT = 0;
        
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                for (int k = maxT; i + k < m && j + k < n; k++) {
                    int i2 = i + k, j2 = j + k;
                    int sum = dp[i2+1][j2+1] - dp[i2+1][j] - dp[i][j2+1] + dp[i][j];
                    if (sum > threshold){
                        break;
                    } else {
                        maxT = Math.max(maxT, k+1);
                    }
                }
            }
        }
        
        return maxT;
        
    }
}