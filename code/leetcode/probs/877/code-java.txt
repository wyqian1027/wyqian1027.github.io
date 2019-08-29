class Solution {
    public boolean stoneGame(int[] piles) {
        // score = score of Alex (turn 0) - score of Bob (turn 1)
        
        int[][][] dp = new int[piles.length+1][piles.length+1][2];
        for (int[][] arr: dp) 
            for (int[] sub: arr) 
                Arrays.fill(sub, -1);
        return score(dp, 0, piles.length - 1, 0, piles) > 0;
    
    }
    
    private int score(int[][][] dp, int l, int r, int turn, int[] piles) {
        
        if (l > r) return 0;
        
        if (dp[l][r][turn] != -1) return dp[l][r][turn];
        
        if (turn == 0) {
            dp[l][r][turn] = Math.max(score(dp, l+1, r, turn^1, piles) + piles[l],
                                      score(dp, l, r-1, turn^1, piles) + piles[r]);
        } else {
            dp[l][r][turn] = Math.min(score(dp, l+1, r, turn^1, piles) - piles[l], 
                                      score(dp, l, r-1, turn^1, piles) - piles[r]);
        }
        
        return dp[l][r][turn];
    }
}