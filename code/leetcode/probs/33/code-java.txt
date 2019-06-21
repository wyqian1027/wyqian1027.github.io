class Solution {
    public int search(int[] nums, int target) {
        
        int lo = 0, hi = nums.length - 1;
        
        while ( lo <= hi ) {
            
            int m = lo + ( hi - lo ) / 2;
            
            if (target == nums[m]) return m;
            
            if (nums[lo] <= nums[m]) {                 
                
                if (nums[lo] <= target && target < nums[m]) {
                    hi = m -1;
                } else {
                    lo = m + 1;
                }
                
            } else {
                
                if (nums[m] < target && target <= nums[hi]) {
                    lo = m + 1;
                } else {
                    hi = m - 1;
                }
            }

        }
        
        return -1;

    }
}