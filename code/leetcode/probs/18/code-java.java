class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
    
        Arrays.sort(nums);
        return helper(nums, target, 0, 4);
    }
    
    private List<List<Integer>> helper(int[] nums, int target, int start, int whatSum){
        
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        int n = nums.length;
        if (n - start < whatSum) return res;
        
        int s1 = 0, s2= 0;
        for (int i = 0; i < whatSum; i++) s1 += nums[start+i];
        for (int i = 0; i < whatSum; i++) s2 += nums[n-1-i];
        if (s1 > target || s2 < target) return res;        
        
        if (whatSum == 2){
            
            int i = start, j = n - 1;
            while (i < j){
                int s = nums[i] + nums[j];
                if (s == target){
                    List<Integer> path = new ArrayList<Integer>();
                    path.add(nums[i]);
                    path.add(nums[j]);
                    res.add(path);
                    while (++i < j && nums[i] == nums[i-1]);
                    while (i < --j && nums[j] == nums[j+1]);
                } else if ( s < target){
                    i++;
                } else {
                    j--;
                }
            }
            
        } else {
            
            for (int i = start; i < n - whatSum + 1; i++){
                if (i != start && nums[i] == nums[i-1]) continue;
                int cur = nums[i];
                List<List<Integer>> sub = helper(nums, target - cur, i + 1, whatSum - 1);
                for(List<Integer> t : sub) {
                   t.add(0, nums[i]);
                }                    
                res.addAll(sub);
            }
        }
        
        return res;
    }
}