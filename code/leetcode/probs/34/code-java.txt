class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        if (nums == null || nums.length == 0) return new int[]{-1, -1};
        int left = -1, right = -1;
        int lo = 0, hi = nums.length - 1;
        
        // search left
        while (lo < hi) {
            int m = lo + (hi-lo) / 2;
            if (target <= nums[m]) {
                hi = m;
            } else {
                lo = m + 1;
            }
        }
        if (nums[lo] != target) return new int[]{left, right};
        left = lo;
        
        // search right
        hi = nums.length - 1;
        while (lo < hi) {
            int m = lo + (hi-lo) / 2 + 1;
            if (target >= nums[m]) {
                lo = m;
            } else {
                hi = m - 1;
            }
        }
        right = hi;
        
        return new int[]{left, right};
    }
}