class Solution {
    public void reverseWords(char[] str) {
        
        if (str == null || str.length == 0) return;
        
        reverse(str, 0, str.length - 1);
        int left = 0;
        for (int right = 0; right < str.length; right++){
            if (right + 1 == str.length || str[right+1] == ' '){
                reverse(str, left, right);
                left = right+2;
            }
        }
    }
    
    public void reverse(char[] str, int i, int j){
        while(i < j){
            char ch = str[i];
            str[i++] = str[j];
            str[j--] = ch;
        }
    }
}