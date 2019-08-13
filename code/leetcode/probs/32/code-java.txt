class Solution {
    public int longestValidParentheses(String s) {
        
        if (s == null || s.length() <= 1) return 0;
        
        char[] arr = s.toCharArray();
        int[] dp = new int[arr.length + 1];  // computes the longest parathesis string ends at idx
        int maxLength = 0;
        
        for (int i = 1; i < s.length(); i++){
            int idx = i + 1;
            if (arr[i-1] == '(' && arr[i] == ')'){
                dp[idx] = dp[idx-2] + 2;
            } else if (arr[i-1] == ')' && arr[i] == ')') {
                int m = dp[idx-1];
                if (i - m - 1 >= 0 && arr[i - m - 1] == '(') {
                    dp[idx] = m + 2 + dp[idx - m - 2];
                }
            }
            maxLength = Math.max(maxLength, dp[idx]);
        }
        return maxLength;
    }
}