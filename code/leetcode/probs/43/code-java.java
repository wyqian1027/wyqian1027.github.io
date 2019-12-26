class Solution {
    public String multiply(String num1, String num2) {
        
        if (num1.equals("0") || num2.equals("0") ) return "0";
        int n1 = num1.length(), n2 = num2.length();
        
        int[] res = new int[n1+n2];
        Arrays.fill(res, 0);
        
        for (int i2 = n2-1; i2 >= 0; i2--){
            for (int i1 = n1-1; i1 >= 0; i1--){
                int digit1 = num1.charAt(i1) - '0'; 
                int digit2 = num2.charAt(i2) - '0'; 
                int product = digit1 * digit2 + res[i1 + i2 + 1];
                res[i1 + i2 + 1] = product % 10;
                res[i1 + i2 ] += product / 10;
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < res.length; i++){
            if (res[i] == 0 && sb.length() == 0) continue;
            sb.append(Integer.toString(res[i]));
        }
        
        return sb.toString();       
    }
}