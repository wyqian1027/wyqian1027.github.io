// 1. Using Collections.swap

class Solution {

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> numList = new ArrayList<>();
        for (int x: nums) numList.add(x);
        
        dfs(numList, res, 0);
        return res;        
    }    
    
    private void dfs(List<Integer> numList, List<List<Integer>> res, int start) {
        
        if (start == numList.size()) {
            res.add(new ArrayList<Integer>(numList));
            return;
        }
        
        for (int i = start; i < numList.size(); i++ ) {
            Collections.swap(numList, start, i);
            dfs(numList, res, start + 1);
            Collections.swap(numList, start, i);
            
        }
    }
}

// 2. Using path.contains() to skip elements

class Solution {

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, new ArrayList<Integer>(), res);
        return res;        
    }
    
    private void dfs(int[] nums, List<Integer> path, List<List<Integer>> res) {
        
        if (path.size() == nums.length) {
            res.add(new ArrayList<Integer>(path));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            
            if (path.contains(nums[i])) continue;
            path.add(nums[i]);
            dfs(nums, path, res);
            path.remove(path.size() - 1);           
            
        }
    }
}