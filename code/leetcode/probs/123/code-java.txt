    public int maxProfit(int[] p) {

        if (p.length <= 1) return 0;
        int K = 3;
        int[][] dp = new int[K][p.length];

        for(int k=1; k < K; k++){
            int min = p[0];
            for(int i=1; i < p.length; i++){
                min = Math.min(min, p[i-1]-dp[k-1][i-1]);
                dp[k][i] = Math.max(dp[k][i-1], p[i]-min);
            }
        }
        return dp[K-1][p.length-1];
    }