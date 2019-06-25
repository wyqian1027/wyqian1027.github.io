// 1. Collections.swap + HashSet
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> numList = new ArrayList<Integer>();
        Arrays.sort(nums);
        for (int x: nums) numList.add(x);
        dfs(0, numList, res);
        return res;        
    }
    
    private void dfs(int start, List<Integer> numList, List<List<Integer>> res){
        
        if (start == numList.size()){
            res.add(new ArrayList<Integer>(numList));
            return;
        }
        
        Set<Integer> appear = new HashSet<>();
        for (int i = start; i < numList.size(); i++){
            if (appear.add(numList.get(i))){
                Collections.swap(numList, start, i);
                dfs(start + 1, numList, res);
                Collections.swap(numList, start, i);            
            }            
        }
    }
}

// 2. Use boolean array to record used or not

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        dfs(nums, new ArrayList<Integer>(), res, new boolean[nums.length]);
        return res;        
    }
    
    private void dfs(int[] nums, List<Integer> path, List<List<Integer>> res, boolean[] used){
        
        if (path.size() == nums.length){
            res.add(new ArrayList<Integer>(path));
            return;
        }
        
        for (int i = 0; i < nums.length; i++){
            if (used[i] || 
                i != 0 && nums[i] == nums[i-1] && !used[i-1]) continue; // use only when previous number is used!

            path.add(nums[i]);
            used[i] = true;
            dfs(nums, path, res, used);
            path.remove(path.size()- 1);
            used[i] = false;
        }
    }
}

