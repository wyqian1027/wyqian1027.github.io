class Solution {
    public int deleteAndEarn(int[] nums) {
        
        if (nums == null || nums.length == 0) return 0;
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int x: nums){
            map.put(x, map.getOrDefault(x , 0)+1);
        }
        
        ArrayList<Integer> keyList = new ArrayList<Integer>(map.keySet());
        Collections.sort(keyList);
        
        int prev = keyList.get(0) - 1;
        int using = 0, avoid = 0;
        int val;
        
        for (int i = 0; i < keyList.size(); i++) {
            
            int key = keyList.get(i);
            if (key - 1 != prev) {
                val = Math.max(using, avoid) + key*map.get(key);
            } else {
                val = avoid +  key*map.get(key);               
            }
            avoid = Math.max(avoid, using);
            using = val;
            prev = key;
        }
        
        return Math.max(avoid, using);
    }
}