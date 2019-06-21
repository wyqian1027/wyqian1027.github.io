// the cleaner way

class Solution {
    public int searchInsert(int[] nums, int target) {
        
        int lo = 0, hi = nums.length - 1;
                
        while ( lo <= hi ){
            
            int m = lo + ( hi - lo ) / 2;
            
            if (nums[m] == target) {
                return m;
                
            } else if ( nums[m] > target ){
                hi = m - 1;
                
            } else {
                lo = m + 1;
            }
            
        }
        return lo;
        
    }
}

// variant

class Solution {

    public int searchInsert(int[] nums, int target) {
        
        int lo = 0, hi = nums.length - 1;

        if (nums[hi] < target) return hi+1;
        
        while ( lo < hi ){
            
            int m = lo + ( hi - lo ) / 2;
            
            if (nums[m] == target) {
                return m;
                
            } else if ( nums[m] > target ){
                hi = m;
                
            } else {
                lo = m + 1;
            }
            
        }
        return lo;
    }
}