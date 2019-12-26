class Solution {

    public int calculate(String s) {
        
        int res = 0;
        int number = 0;
        int sign = 1;
        Stack<Integer> stack = new Stack<>();
        
        for (int i=0; i < s.length(); i++){
            
            char c = s.charAt(i);
            
            if (Character.isDigit(c)){
                number = 10*number + (int)(c - '0');
                
            } else if (c == '+') {
                res += number*sign;
                number = 0;
                sign = 1;
                
            } else if (c == '-') {
                res += number*sign;
                number = 0;
                sign = -1;
                
            } else if (c == '(') {
                stack.push(res);
                stack.push(sign);
                res = 0;
                sign = 1;
            
            } else if (c ==')') {
                res += number*sign;
                res *= stack.pop();
                res += stack.pop();
                number = 0;
            }
            
        }
        
        if (number != 0){
            res += number*sign;
        }
        
        return res;
                
    }
}