class Solution {
    public boolean isIsomorphic(String s, String t) {
        
        Map<Character, Character> map1 = new HashMap<>();
        Map<Character, Character> map2 = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++){
            char charS = s.charAt(i);
            char charT = t.charAt(i);
            if (!map1.containsKey(charS)){
                map1.put(charS, charT);
            } else if (map1.get(charS) != charT) {
                return false;
            }
        }
        
        for (int i = 0; i < s.length(); i++){
            char charS = s.charAt(i);
            char charT = t.charAt(i);
            if (!map2.containsKey(charT)){
                map2.put(charT, charS);
            } else if (map2.get(charT) != charS) {
                return false;
            }
        }
        return true;
    }
    
// Better yet without using maps
class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] m1 = new int[256];
        int[] m2 = new int[256];
        int n = s.length();
        
        for (int i = 0; i < n; i++){
            if (m1[s.charAt(i)] != m2[t.charAt(i)]) return false;
            m1[s.charAt(i)] = i + 1;
            m2[t.charAt(i)] = i + 1;
        }
        return true;
        
    }
    

}