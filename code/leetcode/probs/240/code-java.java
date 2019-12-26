// 2D Binary Search Solution: O(NlogN)
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
        int m = matrix.length, n = matrix[0].length;
        return searchHelper(matrix, target, 0, n-1, 0, m-1);        
    }
    
    private boolean searchHelper(int[][] matrix, int target, int left, int right, int top, int bottom) {
        if (left > right || bottom < top) return false;
        if (target < matrix[top][left] || target > matrix[bottom][right]) return false;
        int row = top;
        int mid = left + (right - left) / 2;
        while (row <= bottom && matrix[row][mid] <= target) {
            if (target == matrix[row][mid]) return true;
            row++;
        }
        return searchHelper(matrix, target, left, mid - 1, row, bottom) || 
            searchHelper(matrix, target, mid + 1, right, top, row - 1);
        
    }
}

// Optimal Walk Solution: O(N)
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return false;
        int m = matrix.length, n = matrix[0].length;
        int r = m - 1, c = 0;
        while (r >= 0 && c <= n-1) {
            if (matrix[r][c] == target) {
                return true;
            } else if (matrix[r][c] < target) {
                c += 1;
            } else {
                r -= 1;
            }
        }
        return false;
    }
}