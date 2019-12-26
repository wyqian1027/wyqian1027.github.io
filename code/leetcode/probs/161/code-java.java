class Solution {
    public boolean isOneEditDistance(String s, String t) {
        
        int lenS = s.length(), lenT = t.length();
        
        if (Math.abs(lenS - lenT) > 1) return false;
        
        for (int i = 0; i < Math.min(lenS, lenT); i++){
            if (s.charAt(i) != t.charAt(i)){
                if (lenS > lenT) {
                    return s.substring(i+1).equals(t.substring(i));
                } else if (lenS == lenT) {
                    return s.substring(i+1).equals(t.substring(i+1));
                } else {
                    return s.substring(i).equals(t.substring(i+1));
                }
            }
        }
        return Math.abs(lenS - lenT) == 1;       
    }
}