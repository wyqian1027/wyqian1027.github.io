class Solution {
    public boolean search(int[] nums, int target) {
        
        
        int lo = 0, hi = nums.length - 1;
        
        while (lo <= hi) {
            
            int m = lo + (hi - lo) / 2;
            
            if (nums[m] == target) return true;
            
            while (lo < m && nums[lo] == nums[m]) lo++;
            
            if (nums[lo] <= nums[m]) {
                
                if (nums[lo] <= target && target < nums[m]) {
                    hi = m - 1;
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
        
        return false;
    }
}