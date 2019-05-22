//memo DFS
class Solution {

    public int findTargetSumWays(int[] nums, int target) {
        
        Map<String, Integer> map = new HashMap<>();
        return dfs(nums, target, 0, 0, map);
    }
    
    private int dfs(int[] nums, int target, int index, int curSum, Map<String, Integer> map) {
        
        String mapKey = index  + "->" + curSum;
        if (map.containsKey(mapKey)){
            return map.get(mapKey);
        }
        
        if (nums.length == index) {
            if (curSum == target) {
                return 1;
            } else {
                return 0;
            }
        }
        
        int val = nums[index];
        int add = dfs(nums, target, index + 1, curSum + val, map);
        int sub = dfs(nums, target, index + 1, curSum - val, map);
        map.put(mapKey, add + sub);
        return add + sub;    
        
    }
}