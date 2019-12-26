class Solution {
    public boolean isPerfectSquare(int num) {
        
        long x = num;
        while (x*x >= num){
            x = (x + num / x) / 2;
            if (x*x == num) return true;
        }
        return false;   
    }
}