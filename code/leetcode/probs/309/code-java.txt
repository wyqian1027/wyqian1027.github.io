class Solution {
    public int maxProfit(int[] p) {
        
        // dp[i] = max( dp[i-1], dp[j-2] + p[i] - p[j] ) for j =0...i-1
        //       = max( dp[i-1], p[i] - (p[j]-dp[j-2]) )
        // ...
        // dp[i] = max( dp[i-1], p[i] - min(p[i-1] - dp[i-3]) )
        // dp[i+1] = max( dp[i], p[i+1] - min(p[i] - dp[i-2]) )
        
        int n = p.length;
        if (n <= 1) return 0;
        int[] dp = new int[n];
        int min = p[0];
        
        for (int i=1; i<n; i++){
            if (i-3 >= 0) {
                min = Math.min(min, p[i-1]-dp[i-3]);
            } else {
                min = Math.min(min, p[i-1]-0);
            }
            dp[i] = Math.max(dp[i-1] , p[i]-min);
        }
        return dp[n-1]; 
    }
}