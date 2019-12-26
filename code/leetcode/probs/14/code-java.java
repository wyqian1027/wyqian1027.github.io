// 1. vertical scanning
class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        if (strs.length == 0) return "";
        
        StringBuilder sb = new StringBuilder();
        int m = strs[0].length();
        int i = 0;
        
        while (i < m) {
            char ch = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++){
                if (i >= strs[j].length() || strs[j].charAt(i) != ch) {
                    return sb.toString();
                }
            }
            sb.append(ch);
            i++;            
        }
        
        return sb.toString();
    }
}

// 2. recursion
class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        if (strs.length == 0) return "";
        
        String pre = strs[0];
        
        for (int i = 1; i < strs.length; i++){
            while (strs[i].indexOf(pre) != 0){
                pre = pre.substring(0, pre.length()-1);
            }
        }
        return pre;
    }
}