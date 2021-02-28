// Solution without using Long..

class Solution {
    
    public int divide(int A, int B) {
        
        if (A == Integer.MIN_VALUE && B == -1) return Integer.MAX_VALUE;
        int a = Math.abs(A), b = Math.abs(B), res = 0, x = 0;
        
        while (a - b >= 0){
            
            for (x = 0; a - (b << x << 1) >= 0; x++);
            
            res += 1 << x;
            
            a -= b << x;
        }
        
        return (A > 0) == (B > 0) ? res : -res;
    }
}

// Alternative, O(32) solution thanks to Lee215:

public int divide(int A, int B) {
    // PS: 1 << 31 == Integer.MIN_VALUE because of overflow
    if (A == 1 << 31 && B == -1) return (1 << 31) - 1;
    int a = Math.abs(A), b = Math.abs(B), res = 0;
    for (int x = 31; x >= 0; x--)
        if ((a >>> x) - b >= 0) {
            res += 1 << x;
            a -= b << x;
        }
    return (A > 0) == (B > 0) ? res : -res;
}
