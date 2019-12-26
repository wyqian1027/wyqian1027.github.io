/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        
        int lo =0, hi = n;
        while (true) {
            
            int m = lo + (hi - lo) / 2;
            
            if (guess(m) == 0) {
                return m;
            } else if (guess(m) < 0) {
                hi = m - 1;
            } else {
                lo = m + 1;
            }
        }
    }
}