class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums); 
        int res = 0;
        for (int i = 2; i < nums.length; i++){
            int j = 0, k = i - 1;
            while (j < k){
                int s = nums[i] + nums[j] + nums[k];
                if (s < target) {
                    res += k - j;
                    j++;
                } else {
                    k--;
                }
            }
        }
        return res;
    }
}