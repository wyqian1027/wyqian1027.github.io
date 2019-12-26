class Solution {
    public boolean isStrobogrammatic(String num) {
        
        if (num == null || num.length() == 0) return true;
        
        int n = num.length();
        
        if (n == 1) return compare(num.charAt(0), num.charAt(0));
        
        return compare(num.charAt(0), num.charAt(n-1)) && isStrobogrammatic(num.substring(1, n-1));
        
    }
    
    public boolean compare(char x, char y){
        
        if (x == '1' && y == '1') return true;
        if (x == '6' && y == '9') return true;
        if (x == '9' && y == '6') return true;
        if (x == '0' && y == '0') return true;
        if (x == '8' && y == '8') return true;
        
        return false;
    }
}