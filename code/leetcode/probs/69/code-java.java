// Newton's Method
class Solution {
    public int mySqrt(int n) {
        
        if (n == 0) return 0;
        long x = n;
        while (x*x > n) {
            x = (n / x + x) / 2;
        }
        return (int) x;
    }
}

// Binary Search, preventing overflows too
class Solution {
    public int mySqrt(int n) {
        
        if (n == 0) return 0;
        int lo = 1, hi = n;
        while (true) {
            int m = lo + (hi - lo)/2;
            if (m > n /m){
                hi = m - 1; 
            } else {
                if ( (m+1) > n / (m+1)){
                    return m;
                }
                lo = m + 1;
            }
        }
    }
}