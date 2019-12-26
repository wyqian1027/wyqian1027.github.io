// O(N) record only max pointer
class Solution {
    
    public boolean canJump(int[] nums){
        
        int max = 0;
        for (int i = 0; i < nums.length; i++){
            if (max < i) return false;
            max = Math.max(max, i+nums[i]);
        }
        return true;
    }    
}

// DP with O(N^2)
class Solution {
    public boolean canJump(int[] nums) {
        
        int n = nums.length;   
        boolean[] dp = new boolean[n];
        dp[0] = true;
        
        for (int i = 1; i < n; i++){
            for (int j = 0; j < i; j++){
                if (dp[j] && nums[j] + j >= i) {
                    dp[i] = true;
                    break;
                } 
            }
            if (!dp[i]) break;
        }
        return dp[n-1];
    }
}