class Solution {
    
    // public static final int[][] directions = new int[][] {{0, 0, 1, -1},{1, -1, 0, 0}};
    
    public void solve(char[][] board) {
        
        if (board == null || board.length == 0 || board[0].length == 0) return;
        int m = board.length, n = board[0].length;
        
        for (int i = 0; i < m; i++){
            if (board[i][0] == 'O') dfs(board, i, 0);
            if (board[i][n-1] == 'O') dfs(board, i, n-1);
        }
        
        for (int j = 0; j < n; j++){
            if (board[0][j] == 'O') dfs(board, 0, j);
            if (board[m-1][j] == 'O') dfs(board, m-1, j);
        }
        
        for (int i = 1; i < m-1; i++){
            for (int j = 1; j < n-1; j++){
                if (board[i][j] == 'O'){
                    board[i][j] = 'X';                  
                }
            }
        }
        
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (board[i][j] == '#'){
                    board[i][j] = 'O';                  
                }
            }
        } 
    }
    
    // turn O to # stemming from borders
    private void dfs(char[][] board, int r, int c){
        
        if (board[r][c] == 'O'){
            board[r][c] = '#';
            if (0 <= r - 1 && board[r-1][c] == 'O') dfs(board, r-1, c);
            if (r + 1 < board.length && board[r+1][c] == 'O') dfs(board, r+1, c);
            if (0 <= c - 1 && board[r][c-1] == 'O') dfs(board, r, c-1);
            if (c + 1 < board[0].length && board[r][c+1] == 'O') dfs(board, r, c+1);
        }
    }
}