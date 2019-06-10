class Solution {
    public int lengthOfLastWord(String s) {
        
        if (s == null) return 0;
        
        int len = 0, prev = 0;
        char[] chars = s.toCharArray();
        
        for (char ch: chars){
            if (ch == ' '){
                len = 0;
            } else {
                len++;
                prev = len;
            }
        }
        return prev;
    }
    
    //alternatively use trim();
    public int lengthOfLastWord(String s) {
        
        return s.trim().length() - 1 - s.trim().lastIndexOf(' ');
        
    }
}