class Solution {
    public boolean canIWin(int maxInt, int total) {
        
        int maxSum = (1 + maxInt)*maxInt/2;
        if (total <= 0) return true;
        if (maxSum < total) return false;
        int[] used = new int[maxInt+1];
        return canIWin(maxInt, total, used, new HashMap<>());
    }
    
    private boolean canIWin(int maxInt, int total, int[] used, HashMap<Integer, Boolean> map){
        
        if (total <= 0) return false;
        // String state = Arrays.toString(used);    // the more general approach
        int state = transform(used);
        if (map.containsKey(state)) return map.get(state);
        
        for (int i = 1; i <= maxInt; i++){
            if (used[i] == 1) continue;
            used[i] = 1;
            if (!canIWin(maxInt, total - i, used, map)) {     // typical minimax game
                map.put(state, true);
                used[i] = 0;
                return true;
            }
            used[i] = 0;
        }
        map.put(state, false);
        return false;    
    }
    
    private int transform(int[] used){      // good if used size is small, here <= 20
        int num = 0;
        for (int x: used){
            num <<= 1;
            if (x == 1) num += 1;
        }
        return num;
    }
}