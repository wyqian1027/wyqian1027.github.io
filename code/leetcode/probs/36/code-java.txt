class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        HashMap<Character, Integer>[] rows = new HashMap[9];
        HashMap<Character, Integer>[] cols = new HashMap[9];
        HashMap<Character, Integer>[] boxes = new HashMap[9];
        for (int i = 0; i < 9; i++){
            rows[i] = new HashMap<Character, Integer>();
            cols[i] = new HashMap<Character, Integer>();
            boxes[i] = new HashMap<Character, Integer>();
        }
        
        for (int r = 0; r < 9; r++){
            for (int c = 0; c < 9; c++){
                if (board[r][c] != '.') {
                    char ch = board[r][c];
                    int index = 3*(r / 3) + c / 3;
                    rows[r].put(ch, rows[r].getOrDefault(ch, 0) + 1);
                    cols[c].put(ch, cols[c].getOrDefault(ch, 0) + 1);
                    boxes[index].put(ch, boxes[index].getOrDefault(ch, 0) + 1);
                    if (rows[r].get(ch) > 1 || cols[c].get(ch) > 1 || boxes[index].get(ch) > 1) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}