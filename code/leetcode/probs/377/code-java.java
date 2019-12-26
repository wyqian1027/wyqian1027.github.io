// bottom up

class Solution {
    public int combinationSum4(int[] nums, int target) {
        
        int[] dp = new int[target + 1];
        Arrays.fill(dp, -1);
        dp[0] = 1;
        
        for (int i = 1; i <= target; i++) {
            
            int s = 0;
            
            for (int j = 0; j < nums.length; j++) {
                // finding combo ending with nums[j], no repetition!
                if (i - nums[j] >= 0) {
                    s += dp[i - nums[j]];
                }
            }
            
            dp[i] = s;
        }
        
        return dp[target];
    
    }
}

// top down
class Solution {
    public int combinationSum4(int[] nums, int target) {
        
        int[] dp = new int[target+1];
        Arrays.fill(dp, -1);
        dp[0] = 1;
        
        return calculate(target, nums, dp);
    }
    
    private int calculate(int target, int[] nums, int[] dp) {
        
        if (target < 0) return 0;
        
        if (dp[target] != -1) return dp[target];
        
        int s = 0;
        
        for (int i = 0; i < nums.length; i++){
            s += calculate(target - nums[i], nums, dp);
        }
        
        dp[target] = s;
        return s;
    }
}