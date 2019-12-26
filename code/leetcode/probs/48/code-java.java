class Solution {
    public void rotate(int[][] matrix) {
        
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return;
        transpose(matrix);
        reverseRows(matrix);
    }
    
    private void transpose(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = i + 1; j < n; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
    }
    
    private void reverseRows(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n - 1 - j; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][n-1-j];
                matrix[i][n-1-j] = tmp;
            }
        }
    }
}