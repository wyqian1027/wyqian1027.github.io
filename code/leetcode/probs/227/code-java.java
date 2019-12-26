class Solution {

    public int calculate(String s) {
        
        Stack<Integer> stack = new Stack<>();
        int number = 0;
        char sign = '+';
        
        for (int i=0; i < s.length(); i++) {
            
            char c = s.charAt(i);
            
            if (Character.isDigit(c)) {
                number = 10 * number + (int)(c-'0');
            } 
            
            if (!Character.isDigit(c) && ' ' != c || i == s.length()-1) {
            
                if (sign == '+') {
                    stack.push(number);
                
                } else if (sign == '-') {
                    stack.push(-number);
                
                } else if (sign == '*') {
                    stack.push(stack.pop()*number);
                
                } else if (sign == '/') {
                    stack.push(stack.pop()/number);
                    
                }
                
                sign = c;
                number = 0;               
            } 
        }
        
        int res = 0;
        for (int x: stack) {
            res += x;
        }
        return res;    
    }
    
}