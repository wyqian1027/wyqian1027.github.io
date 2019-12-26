class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        
        int moves = 0;
        while (m != n){
            m >>= 1;
            n >>= 1;
            moves += 1;
        }
        return m << moves;
    }
}