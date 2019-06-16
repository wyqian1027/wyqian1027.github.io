class Solution {
    public int romanToInt(String s) {
        
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        
        char prev = 'I';
        int sum = 0;
        for (int i = s.length() - 1; i >= 0; i--){
            char cur = s.charAt(i);
            if (map.get(prev) <= map.get(cur)){
                sum += map.get(cur);
            } else {
                sum -= map.get(cur);
            }
            prev = cur;           
        }
        
        return sum;
    }
}