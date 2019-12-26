class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        Map< Integer, Integer > map = new HashMap<>();
        for (int[] arr: dominoes){
            int k = Math.min(arr[0], arr[1])*10 + Math.max(arr[0], arr[1]);
            map.put(k, map.getOrDefault(k, 0) + 1);
        }
        int s = 0;
        for (int val: map.values()){
            s += val*(val-1) / 2;
        }
        return s;
    }
}