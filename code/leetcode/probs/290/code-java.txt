// Using Map and Set O(n)
class Solution {
    public boolean wordPattern(String pattern, String str) {
        
        String[] strArr = str.split(" ", -1);
        if (pattern.length() != strArr.length) return false;
        
        char[] patternArr = pattern.toCharArray();
        
        Map<Character, String> map = new HashMap<>();
        Set<String> set = new HashSet<>();
        
        for (int i=0; i < strArr.length; i++){
            
            if (!map.containsKey(patternArr[i])){
                
                if (set.contains(strArr[i])) return false;
                
                map.put(patternArr[i], strArr[i]);
                set.add(strArr[i]);

            } else if (!map.get(patternArr[i]).equals(strArr[i])){
                
                return false;
            }
        }
        return true;
    }
}