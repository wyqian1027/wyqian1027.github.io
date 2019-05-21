class Solution {

    public int evalRPN(String[] tokens) {
     
        Stack<Integer> stack = new Stack<>();
        
        for (String x: tokens) {
            
            if (x.equals("+")) {
                stack.push(stack.pop() + stack.pop());                
            } else if (x.equals("-")) {
                stack.push( - stack.pop() + stack.pop());
            } else if (x.equals("*")) {
                stack.push(stack.pop() * stack.pop());  
            } else if (x.equals("/")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a / b);
            } else {
                stack.push(Integer.parseInt(x, 10));
            }
        }
        
        return stack.pop();
    }
}