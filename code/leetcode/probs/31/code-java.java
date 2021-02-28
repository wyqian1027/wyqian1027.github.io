class Solution {
    public void nextPermutation(int[] nums) {
        // 1 2 3_4_6 5 5 2
        // 1 2 3 5 2 4 5 6
        // 1) find reversed subarray and the anomaly
        // 2) swap the first higher number with anomaly
        // 3) reverse the subarray
	// 4) if not, reverse the entire array
        if (nums == null || nums.length <= 1) return;
        for (int i=nums.length-2; i>=0; i--) {
            if (nums[i] < nums[i+1]) {
                int j = nums.length-1;
                while (j > i && nums[i] >= nums[j]) j--;
                swap(nums, i, j);
                reverse(nums, i+1, nums.length-1);
                return;
            }
        }
        reverse(nums, 0, nums.length-1);
    }
    
    public void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    public void reverse(int[] nums, int i, int j) {
        while (i < j) {
            swap(nums, i++, j--);
        }
    }
}
