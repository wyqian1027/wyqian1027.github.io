// 1. Same Logic as Subset I, manually deal with repetitions

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        
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
        
        int rep = 1;
        while (start + rep < nums.length && nums[start + rep] == nums[start]){
            rep++;    
        }
        
        for (int i = 0; i < rep; i++){
            path.add(nums[start]);
            dfs(nums, start+rep, path, res);
        }
        for (int i = 0; i < rep; i++){
            path.remove(path.size()-1);
        }
        
        dfs(nums, start+rep, path, res);
        
    }

}

// 2. Pick the element at right location in each DFS

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        
        dfs(nums, 0, new ArrayList<Integer>(), res);
        return res;
    }
    
    private void dfs(int[] nums, int start, List<Integer> path, List<List<Integer>> res) {
        
        res.add(new ArrayList<>(path));

        for (int i = start; i < nums.length; i++){

            if (i != start && nums[i] == nums[i-1]) continue;

            path.add(nums[i]);
            dfs(nums, i+1, path, res);
            path.remove(path.size() - 1);
        }    
    }

}