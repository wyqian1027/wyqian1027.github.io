class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length;
        
        if (n < 3) return res;
        
        for (int i = 0; i < n - 2; i++){
            if (i != 0 && nums[i] == nums[i-1]) continue;
            int j = i + 1;
            int k = n - 1;
            while (j < k){
                int s = nums[i] + nums[j] + nums[k];
                if (s == 0){
                    res.add(new ArrayList<Integer>(Arrays.asList(nums[i], nums[j], nums[k])));
                    while (++j < k && nums[j] == nums[j-1]);
                    while (j < --k && nums[k] == nums[k+1]);
                    
                } else if (s < 0){
                    j++;
                    
                } else {
                    k--;
                }
            }
        }
        return res;
        
    }
}