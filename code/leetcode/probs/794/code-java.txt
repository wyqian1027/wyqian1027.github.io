class Solution {
    public boolean validTicTacToe(String[] board) {
        String game = board[0] + board[1] + board[2];

        int firstCount = countChar(game, 'X');
        int secondCount = countChar(game, 'O');
        // System.out.println(game);
        // System.out.println(game);
        // System.out.println(firstCount + ", " + secondCount);
        if (firstCount -1 != secondCount && firstCount != secondCount) return false;
        if (firstCount == secondCount && isWinning(board, 'X')) return false;
        if (firstCount -1 == secondCount && isWinning(board, 'O')) return false;
        return true;
    }
    
    public int countChar(String str, char c)
    {
        int count = 0;
        for(int i=0; i < str.length(); i++)
        {    if(str.charAt(i) == c)
                count++;
        }
        return count;
    }
    
    public boolean isWinning(String[] board, char c) {
        for (int i=0; i<3; i++){
            if (board[i].charAt(0) == c && board[i].charAt(1) == c && board[i].charAt(2) == c ) return true;
            if (board[0].charAt(i) == c && board[1].charAt(i) == c && board[2].charAt(i) == c ) return true;
        }
        if (board[0].charAt(0) == c && board[1].charAt(1) == c && board[2].charAt(2) == c )  return true;
        if (board[0].charAt(2) == c && board[1].charAt(1) == c && board[2].charAt(0) == c )  return true;
        return false;
    }
    
}