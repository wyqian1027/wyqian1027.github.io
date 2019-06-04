class Solution {
    public int minPatches(int[] nums, int n) {
        int patches = 0, i = 0;
        long miss = 1;
        
        while (miss <= n) {
            if (i < nums.length && nums[i] <= miss) {
                miss += nums[i];
                i++;
            } else {
                miss += miss;
                patches++;
            }
        }
        return patches;
    }
}