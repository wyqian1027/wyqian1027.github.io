class Solution {
    public int myAtoi(String str) {
        str = str.trim();
        boolean isPositive = true;
        boolean signed = false;
        int res = 0;
        int i = 0;
        
        while (i < str.length()) {
            char ch = str.charAt(i);
            if (Character.isDigit(ch)) {
                int x = Character.getNumericValue(ch);               
                signed = true;
                if ((Integer.MAX_VALUE / 10 < res ) || (Integer.MAX_VALUE / 10 == res && Integer.MAX_VALUE % 10 < x)){
                    return isPositive ? Integer.MAX_VALUE : Integer.MIN_VALUE;
                }
                 res = res*10 + x;
            } else if (!signed && (ch == '+' || ch == '-')) {
                isPositive = ch == '+' ? true : false;
                signed = true;
            } else {
                break;
            }
            i++;
        }
        
        return isPositive ? res : -res;
    }
}