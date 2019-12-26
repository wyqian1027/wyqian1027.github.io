// Improve by passing index instead of list slicing
class Solution {
    public List<List<Integer>> subsets(int[] nums) {

        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        
        dfs(nums, 0, new ArrayList<Integer>(), res);
        return res;
    }
    
    private void dfs(int[] nums, int start, List<Integer> path, List<List<Integer>> res) {
        
        if (start == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }
        
        dfs(nums, start+1, path, res);
        path.add(nums[start]);
        dfs(nums, start+1, path, res);
        path.remove(path.size()-1);
    }
}