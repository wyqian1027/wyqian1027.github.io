class Solution {

    // two dictionary
    public boolean canConstruct(String ransomNote, String magazine) {
        
        int[] ransomMap = new int[26];
        int[] magMap = new int[26];
        
        char[] ransomChars = ransomNote.toCharArray();
        char[] magChars = magazine.toCharArray();
        
        for (char ch: ransomChars) ransomMap[ch - 'a']++;
        for (char ch: magChars) magMap[ch - 'a']++;
        for (int i=0; i< 26; i++){
            if (ransomMap[i] > magMap[i]) return false;
        }
        return true;
    }
    
    // or just one dictionary
    public boolean canConstruct(String ransomNote, String magazine) {
        
        int[] magMap = new int[26];
        
        char[] ransomChars = ransomNote.toCharArray();
        char[] magChars = magazine.toCharArray();
        
        for (char ch: magChars) magMap[ch - 'a']++;
        for (char ch: ransomChars) {
            if (--magMap[ch - 'a'] < 0) return false;
        }

        return true;
    }
}