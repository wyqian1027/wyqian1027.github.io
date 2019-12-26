class Solution {

    public int findMin(int[] nums) {
        
        int lo = 0, hi = nums.length - 1;
        
        while (lo < hi) {
            int m = lo + (hi - lo) / 2;
            while (m < hi && nums[m] == nums[hi]) hi--;
            if (nums[m] > nums[hi]) {  
                lo = m + 1;
            } else if (nums[m] < nums[hi])  {  
                hi = m;            
            }
        }
        
        return nums[lo];    
    } 
}