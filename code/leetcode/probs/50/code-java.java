
// Power trick
class Solution {
    public double myPow(double x, int n) {
        
        if (n == 0) return 1;

        if (n < 0) {
            return 1/x*myPow(1/x, -(n+1));
        }
        
        double res = 1;
        while (n > 0){
            
            if ((n & 1) == 1) {
                res *= x;    
            }
            x *= x;
            n = n >> 1;
        }
        return res;
    }
}

//Recursion:
class Solution {
    public double myPow(double x, int n) {
        
        if (n == 0) return 1;
        else if (n < 0) {
            return myPow(1/x, -(n+1))*1/x;            
        }
        
        double half = myPow(x, n / 2);
        
        return (n % 2 == 1 ? half*half*x : half*half);
    }
}