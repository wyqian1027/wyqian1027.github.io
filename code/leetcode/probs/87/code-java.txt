class Solution {
    public boolean isScramble(String s1, String s2) {
        
        if (s1 == null && s2 == null) return true;
        if (s1.length() != s2.length()) return false;
        if (s1.equals(s2)) return true;
        
        int[] map = new int[26];
        int n = s1.length();
        for (int i=0; i < n; i++) map[s1.charAt(i) - 'a']++;
        for (int i=0; i < n; i++) {
            if (--map[s2.charAt(i) - 'a'] < 0) return false;
        }
        
        for (int i=1; i < n; i++){
            if (isScramble(s1.substring(0, i), s2.substring(0, i)) &&
                isScramble(s1.substring(i, n), s2.substring(i, n))) return true;
            if (isScramble(s1.substring(0, i), s2.substring(n-i, n)) &&
                isScramble(s1.substring(i, n), s2.substring(0, n-i))) return true;
        }
        return false;
    }
}