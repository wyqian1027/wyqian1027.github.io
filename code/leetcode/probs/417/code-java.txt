class Solution {
    
    int[][] dirs = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return new ArrayList<>();
        }
        
        int m = matrix.length, n = matrix[0].length;
        List<List<Integer>> ans = new ArrayList<>();
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        
        for (int i = 0; i < m; i++) dfs(i, 0, matrix[i][0], pacific, matrix);
        for (int j = 0; j < n; j++) dfs(0, j, matrix[0][j], pacific, matrix);
        for (int i = 0; i < m; i++) dfs(i, n-1, matrix[i][n-1], atlantic, matrix);
        for (int j = 0; j < n; j++) dfs(m-1, j, matrix[m-1][j], atlantic, matrix);
        
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (pacific[i][j] && atlantic[i][j]) {
                    List<Integer> pair = new ArrayList<>();
                    pair.add(i);
                    pair.add(j);
                    ans.add(pair);
                }
            }
        }
        return ans;
    }
    
    private void dfs(int r, int c, int height, boolean[][] visited, int[][] matrix){
        
        int m = matrix.length, n = matrix[0].length;
        
        if (r < 0 || r >= m || c < 0 || c >= n || visited[r][c] || matrix[r][c] < height)
            return;
        visited[r][c] = true;
        for (int[] d: dirs){
            dfs(r+d[0], c+d[1], matrix[r][c], visited, matrix);
        }
    }
}