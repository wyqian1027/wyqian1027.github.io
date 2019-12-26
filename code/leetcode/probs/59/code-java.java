class Solution {
    public int[][] generateMatrix(int n) {
    
        int[] DIRR = new int[] {0, 1, 0, -1};
        int[] DIRC = new int[] {1, 0, -1, 0};
        int[][] matrix = new int[n][n];
        int num = 1;
        int r = 0, c = 0;
        int d = 0;
        
        while (num <= n*n) {
            
            matrix[r][c] = num;
            if (0 <= r + DIRR[d] && r + DIRR[d] < n && 0 <= c + DIRC[d] && c + DIRC[d] < n && 
                matrix[r + DIRR[d]][c + DIRC[d]] == 0) {
                r += DIRR[d];
                c += DIRC[d];
            } else {
                d = (d + 1) % 4;
                r += DIRR[d];
                c += DIRC[d];
            }
            num += 1;
        }
        
        return matrix;
    }
}