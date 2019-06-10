class Solution {
    public int strStr(String haystack, String needle) {
        
        if (needle == null || needle.length() == 0) return 0;
        int l1 = haystack.length(), l2 = needle.length();
        if (l2 > l1) return -1;
        
        for (int i = 0; i < l1 - l2 + 1; i++) {
            
            if (haystack.substring(i, i + l2).equals(needle)){
                return i;
            }
        }
        return -1;
    }
}