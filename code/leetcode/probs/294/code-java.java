// Backtrack Solution
class Solution {
    public boolean canWin(String s) {
        
        if (s == null || s.length() < 2) return false;
        
        char[] arr = s.toCharArray();
        for (int i=0; i < arr.length-1; i++){
            if (arr[i] == '+' && arr[i+1] == '+'){
                arr[i] = arr[i+1] = '-';
                if (!canWin(new String(arr))) return true;
                arr[i] = arr[i+1] = '+';
            }
        }
        return false;
    }
}

// With Memorization
class Solution {
    public boolean canWin(String s) {
        Map<String, Boolean> map = new HashMap<>();
        return canWin(s, map);
        
    }
    
    public boolean canWin(String s, Map<String, Boolean> map){
        
        if (s == null || s.length() < 2) return false;
        
        if (map.containsKey(s)) return map.get(s);
        
        char[] arr = s.toCharArray();
        
        for (int i=0; i < arr.length-1; i++){
            if (arr[i] == '+' && arr[i+1] == '+'){
                arr[i] = arr[i+1] = '-';
                if (!canWin(new String(arr), map)) {
                    map.put(s, true);
                    return true;
                }
                arr[i] = arr[i+1] = '+';
            }
        }
        map.put(s, false);
        return false;
    }

}