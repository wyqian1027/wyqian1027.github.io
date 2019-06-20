class Solution {
    
    List<List<String>> res = new ArrayList<>();
    
    public List<List<String>> solveNQueens(int n) {
        
        char[][] board = new char[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(board[i], '.');
        dfs(board, 0, 0);
        return res;        
    }
    
    private void add(char[][] board){
        
        List<String> snapshot = new ArrayList<>();
        for (int i = 0; i < board.length; i++){
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < board.length; j++){
                sb.append(board[i][j]);
            }
            snapshot.add(sb.toString());            
        }
        res.add(snapshot);
    }
    
    private void dfs(char[][] board, int r, int c){
        
        if (r == board.length) {
            add(board);
            return;
        }
        
        // if valid, check next row
        // if (checkH(board, r, c) && checkV(board, r, c) && checkD(board, r, c)){
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
    
    // borrowed from solution
    private boolean validate(char[][] board, int x, int y) {
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board.length; j++) {
                if(board[i][j] == 'Q' && (x + j == y + i || x + y == i + j || x == i || y == j))
                    return false;
            }
        }
        return true;
    }
    
    private boolean checkH(char[][] board, int r, int c){
        
        for (int i = 0; i < board.length; i++){
            if (board[r][i] == 'Q') return false;
        }
        return true;
    }
    
    private boolean checkV(char[][] board, int r, int c){
        
        for (int i = 0; i < board.length; i++){
            if (board[i][c] == 'Q') return false;
        }
        return true;
    }
    
    private boolean checkD(char[][] board, int r, int c){
        
        int n = board.length;
        for (int i = 1; i < board.length && r - i >= 0 && c - i >= 0; i++){
            if (board[r-i][c-i] == 'Q') return false;
        }
        for (int i = 1; i < board.length && r + i < n && c + i < n; i++){
            if (board[r+i][c+i] == 'Q') return false;
        }
        for (int i = 1; i < board.length && r + i < n && c - i >= 0; i++){
            if (board[r+i][c-i] == 'Q') return false;
        }
        for (int i = 1; i < board.length && r - i >= 0 && c + i < n; i++){
            if (board[r-i][c+i] == 'Q') return false;
        }
        return true;    
    }
}