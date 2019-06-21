/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    
    public int firstBadVersion(int n) {
        
        int lo = 1, hi = n;
        int m = n;
        
        while (lo < hi) {
            
            m = lo + (hi - lo) / 2;
            
            if (isBadVersion(m)){
                hi = m;
            } else {
                lo = m + 1;
            }
        }
        
        return lo;
    }
}