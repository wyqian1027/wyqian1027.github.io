class Solution {
    public int minPathSum(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int[][] res = new int[rows][cols];
        
        int temp = 0;
        for (int r = 0; r < rows; r++){
            temp += grid[r][0];
            res[r][0] = temp;
        }
        temp = 0;
        for (int c = 0; c < cols; c++){
            temp += grid[0][c];
            res[0][c] = temp;
        }
        
        for (int r = 1; r < rows; r++){
            for (int c = 1; c < cols; c++){
                res[r][c] = Math.min(res[r-1][c], res[r][c-1]) + grid[r][c];
            }
        }
        return res[rows-1][cols-1];
    }
}