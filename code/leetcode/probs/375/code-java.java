class Solution {
    public int getMoneyAmount(int n) {
        
        int[][] dp = new int[n+1][n+1];
        for (int[] row: dp) Arrays.fill(row, -1);
        return calculate(1, n, dp);
    }
    
    private int calculate(int lo, int hi, int[][] dp){
        if (lo >= hi) return 0;
        if (dp[lo][hi] != -1) return dp[lo][hi];
        int res = Integer.MAX_VALUE;
        for (int i = lo + (hi - lo)/2; i <= hi; i++){ // further optimization from i = lo
            int cost = i + Math.max(calculate(lo, i-1, dp), calculate(i+1, hi, dp));
            res = Math.min(res, cost);
        }
        dp[lo][hi] = res;
        return res;
    }
}