class Solution {
        
    private int res = 0;
    
    public int totalNQueens(int n) {
        char[][] board = new char[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(board[i], '.');
        dfs(board, 0, 0);
        return res;        
    }
    
    private void add(char[][] board){
        res += 1;
    }
    
    private void dfs(char[][] board, int r, int c){

	if (r == board.length) {
            add(board);
            return;
        }
        
        // if valid, check next row
        if (validate(board, r, c)){
            board[r][c] = 'Q';
            dfs(board, r+1, 0);
            board[r][c] = '.';
        }
        // if this row has unchecked col, go to the next col
        if (c + 1 < board.length) {
            dfs(board, r, c+1);
        } 
    }
    
    // borrow ideas from discussion:
    private boolean validate(char[][] board, int x, int y) {
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board.length; j++) {
                if(board[i][j] == 'Q' && (x + j == y + i || x + y == i + j || x == i || y == j))
                    return false;
            }
        }
        return true;
    }
}
