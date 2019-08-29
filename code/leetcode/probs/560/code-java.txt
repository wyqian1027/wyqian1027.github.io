class Solution {
    public int subarraySum(int[] nums, int k) {
        int acc = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int res = 0;
        for (int num: nums) {
            acc += num;
            if (map.containsKey(acc - k)){
                res += map.get(acc - k);   
            }
            map.put(acc, map.getOrDefault(acc, 0) + 1);
        }
        return res;
        
    }
}