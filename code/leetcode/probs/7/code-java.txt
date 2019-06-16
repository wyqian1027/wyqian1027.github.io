class Solution {
    public int reverse(int x) {
        
        int ans = 0;      
        
        while (x != 0) {
            int rem = x % 10;
            //Option 1: HardCoding:
            // if (ans > Integer.MAX_VALUE/10 || (ans == Integer.MAX_VALUE/10 && rem > 7)) return 0;
            // if (ans < Integer.MIN_VALUE/10 || (ans == Integer.MIN_VALUE/10 && rem < -8)) return 0;
            // ans = ans*10 + rem;
            
            //Option 2: Checking overflow by rolling back to see if results are consistent.
            int newResult = ans*10 + rem;
            if ((newResult - rem) / 10 != ans) return 0;
            ans = newResult;
            x /= 10;
            
        }
        return ans;
    }
}