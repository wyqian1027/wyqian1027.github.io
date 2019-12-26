class Solution {
    public String addBinary(String a, String b) {
        
        StringBuilder sb = new StringBuilder();
        int n1 = a.length(), n2 = b.length();
        int i1 = n1 - 1, i2 = n2 - 1;
        
        int carry = 0;
        while (i1 >= 0 || i2 >= 0){
            char cur1 = '0';
            char cur2 = '0';
            if (i1 >= 0) cur1 = a.charAt(i1);
            if (i2 >= 0) cur2 = b.charAt(i2);
            int sum = carry + cur1 - '0' + cur2 - '0';
            int digit = sum % 2;
            carry = sum / 2;
            sb.append(digit);
            i1--;
            i2--;
        }
        if (carry == 1) sb.append("1");
        
        return sb.reverse().toString();
    }
}