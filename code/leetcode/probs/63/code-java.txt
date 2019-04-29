class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int cols = obstacleGrid[0].length, rows = obstacleGrid.length;
        if (obstacleGrid[0][0] == 1 || obstacleGrid[rows-1][cols-1] == 1) return 0;
        int[] dp = new int[cols+1];
        
        for (int r=1; r < rows+1; r++){
            dp[0] = (r==1? 1: 0);
            for (int c=1; c < cols+1; c++){
                if (obstacleGrid[r-1][c-1] != 1) {
                    dp[c] = dp[c] + dp[c-1];
                } else {
                    dp[c] = 0;
                }
            }
        }
        return dp[cols];
        
    }
}