class Solution {
    public void nextPermutation(int[] nums) {
        
        int n = nums.length;
        int left = -1;
        
        for (int i = n-2; i >= 0; i--) {
            if (nums[i] < nums[i+1]){
                left = i;
                break;
            }
        }
        if (left == -1) {
            reverse(nums, 0, n-1);
            return;
        }

        int right = n;
        for (int i = n-1; i > left; i--){
            if (nums[i] > nums[left]){
                right = i;
                break;
            }
        }
        swap(nums, left, right);
        reverse(nums, left+1, n-1);
 
    }
    
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    private void reverse(int[] nums, int i, int j){
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }
    
}