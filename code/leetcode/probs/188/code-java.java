    public int maxProfit(int[] p, int trans) {

        if (p.length <= 1) return 0;

        //special case, we can just add anything we want
        if (trans >= p.length/2){
            int profit = 0, prev = p[0];
            for (int i=1; i < p.length; i++) {
                int cur = p[i];
                if (prev < cur) profit+=cur-prev;
                prev = cur;
            }
            return profit;
        }

        //DP from 123
        int K = trans+1;
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