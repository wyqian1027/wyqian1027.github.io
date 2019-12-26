class Solution {

    public int calculate(String s) {
        
        if (s == null || s.length() == 0) return 0;
        
        Stack<Character> operators = new Stack<>();
        Stack<Integer> numbers = new Stack<>();
        int num = 0;
        
        for (int i = 0; i < s.length(); i++ ) {
            
            char c = s.charAt(i);
            
            if (c == ' ') continue;
            
            if (Character.isDigit(c)) {
                num = (int)(c-'0');
                while (i + 1 < s.length() && Character.isDigit(s.charAt(i+1))) {
                    num = 10*num + (int) (s.charAt(i+1) - '0');
                    i++;
                }
                numbers.push(num);
                num = 0;
            
            } else if (c == '(') {
                operators.push(c);    
                
            } else if (c == ')') {
                while (operators.peek() != '(') {
                    numbers.push(operations(operators.pop(), numbers.pop(), numbers.pop()));
                }
                operators.pop();
                
            } else if (c == '+' || c == '-' || c == '*' || c == '/') {
                while (!operators.isEmpty() && checkPrecedence(c, operators.peek())) {
                    numbers.push(operations(operators.pop(), numbers.pop(), numbers.pop()));
                }
                 operators.push(c);  
            }
        }
        
        while (!operators.isEmpty()) {
            numbers.push(operations(operators.pop(), numbers.pop(), numbers.pop()));
        }
        return numbers.pop();
    }

    private int operations(char operator, int b, int a) {
        
        switch(operator) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a*b;
            case '/': return a/b;
            default: return 0;                
        }       
    }

    private boolean checkPrecedence(char curOperator, char prevOperator) {
        
        if (prevOperator == '(' || prevOperator == ')') {
            return false;
        } 
        
        if ((prevOperator == '+' || prevOperator == '-') && (curOperator == '*' || curOperator == '/')){
            return false;
        }
        
        return true;
    }

}