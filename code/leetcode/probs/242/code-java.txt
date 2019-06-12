class Solution {
    public boolean isAnagram(String s, String t) {
        
        if (s.length() != t.length()) return false;
        int n = s.length();
        int[] map = new int[26];
        
        for (int i = 0; i < n; i++){
            map[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < n; i++){
            map[t.charAt(i) - 'a']--;
        }
        for (int i: map){
            if (i != 0) return false;
        }
        return true;
    }
}