class Solution {
    public double largestSumOfAverages(int[] A, int K) {
        
        int n = A.length;
        double[][] dp = new double[K][n];
        double[] acc = new double[n];
        
        double cur = 0;
        for (int i = 0; i < n; i++){
            cur += A[i];
            acc[i] = cur;
            dp[0][i] = cur / (i + 1);
        }
        
        double max_sum = dp[0][n-1];
        for (int k = 1; k < K; k++) {
            for (int i = k; i < n; i++){
                double cur_max = Double.MIN_VALUE;
                for (int j = k-1; j < i; j++) {
                    cur_max = Math.max(cur_max, dp[k-1][j] + (acc[i] - acc[j]) / (i - j));
                }
                dp[k][i] = cur_max;
            }
            max_sum = Math.max(max_sum, dp[k][n-1]);
        }
        return max_sum;
    }
}