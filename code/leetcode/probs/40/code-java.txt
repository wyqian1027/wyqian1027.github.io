class Solution {
    public List<List<Integer>> combinationSum2(int[] nums, int target) {
        
        Arrays.sort(nums);
        
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, 0, target, new ArrayList<Integer>(), res);
        return res;
    }
    
    private void dfs(int[] nums, int start, int target, List<Integer> path, List<List<Integer>> res){
        
        if (target == 0){
            
            res.add(new ArrayList<Integer>(path));
            return;
        }
        
        for (int i = start; i < nums.length; i++){
            
            if (i != start && nums[i] == nums[i-1]) continue;
            
            if (target - nums[i] >= 0) {
                
                path.add(nums[i]);
                dfs(nums, i+1, target - nums[i], path, res);    // only place of different to #39. 
                path.remove(path.size() - 1);
                
            }
        }
    }

}