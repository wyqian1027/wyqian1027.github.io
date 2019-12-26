class Solution {

    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++){
            
            int x = nums[i];
            
            if (map.containsKey(x)){
                
                return new int[] {map.get(x), i};
                
            } else {
                
                map.put(target - x, i);
                
            }
            
        }
        
        return new int[] {-1, -1};
         
    }

}