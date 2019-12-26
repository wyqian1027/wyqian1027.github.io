class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, 0, new ArrayList<Integer>(), res);
        return res;
    }
    
    private void dfs(int[] nums, int start, List<Integer> path, List<List<Integer>> res){
        
        if (path.size() >= 2){
            res.add(new ArrayList<Integer>(path));
        }
        
        Set<Integer> set = new HashSet<>();        
        for (int i = start; i < nums.length; i ++){
            if (set.contains(nums[i])) continue;
            if ((path.size() == 0 ) || (nums[i] >= path.get(path.size() - 1))) {
                path.add(nums[i]);
                set.add(nums[i]);
                dfs(nums, i+1, path, res);
                path.remove(path.size()-1);
            }
        }
    }
}