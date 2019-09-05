# Even better! No need for dictionary!
class Solution {
    public int lenLongestFibSubseq(int[] A) {
        
        int[][] dp = new int[A.length][A.length];
        int ans = 0;
        
        for (int i = 2; i < A.length; i++) {
            int l = 0;
            int r = i - 1;
            while (l < r) {
                int sum = A[l] + A[r] - A[i];
                if (sum < 0) l++;
                else if (sum > 0) r--;
                else {
                    dp[r][i] = dp[l][r] + 1;
                    ans = Math.max(dp[r][i], ans);
                    l++; r--;
                }
            }
        }
        return ans > 0 ? ans + 2: 0;
    }
}