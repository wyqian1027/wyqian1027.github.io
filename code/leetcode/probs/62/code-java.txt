// Preferred way of using Factorials!!!
class Solution {
    
    public int uniquePaths(int m, int n){
    
        double res = 1; // very important 
        int N = m + n - 2;
        int K = m - 1;
        
        // notice the order. matching smallest factors in numerator/denominator
        for (int i = 1; i <= K; i++){
            res = res* (N - K + i) / i;
        }
        
        return (int) res;
    
    }
}

class Solution {
    public int uniquePaths(int m, int n) {
        
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        
        for (int i = 1; i < m; i++){
            for (int j = 1; j < n; j++){
                dp[j] = dp[j] + dp[j-1];   // above and left
            }
        }        
        return dp[dp.length - 1];
    }
}
    
