// Using Reverse functions

class Solution {

    public void rotate(int[] nums, int k) {
        
        if ((nums == null) || (nums.length == 0) || (k == 0)) return;
        
        k %= nums.length;
        
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
        
    }
    
    public void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    public void reverse(int[] nums, int start, int end){ // inclusiveee
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
    
}