// TOP DOWN
class Solution {
    public int maxCoins(int[] nums) {
    
        int n = nums.length + 2;
        int[] nums2 = new int[n];
        nums2[0] = 1;
        for (int i = 0; i < nums.length; i++) nums2[i+1] = nums[i];
        nums2[nums.length+1] = 1;
        
        int[][] dp = new int[n][n];
        return maxCoin(nums2, 0, n-1, dp);
     }
    
    public int maxCoin(int[] nums, int start, int end, int[][] dp){
    // max coin inside (start, end) exclusive endpoints
    
        if (start + 1 >= end) return 0;
        
        if (dp[start][end] != 0) return dp[start][end];
        
        int res = 0;
        for (int i = start + 1; i <= end-1; i++){
            res = Math.max(res, nums[i]*nums[start]*nums[end] +
                           maxCoin(nums, start, i, dp) + maxCoin(nums, i, end, dp));
        }
        
        dp[start][end] = res;
        return res;
    }
}

// BOTTOM UP
class Solution {    
    public int maxCoins(int[] nums) {
        
        int n = nums.length + 2;
        int[] nums2 = new int[n];
        nums2[0] = 1;
        for (int i = 0; i < nums.length; i++) nums2[i+1] = nums[i];
        nums2[nums.length+1] = 1;
        
        int[][] dp = new int[n][n];
        
        for (int gap = 2; gap <= n-1; gap++){
            for (int start = 0; start <= n - 1 - gap; start++){
                int end = start + gap;
                for (int k = start + 1; k < start + gap; k++){
                    dp[start][end] = Math.max(dp[start][end], nums2[start]*nums2[k]*nums2[end] +
                                  dp[start][k] + dp[k][end]);
                }
            }
        }
        return dp[0][n-1];
    }
}