class MinStack {

    private Stack<Integer> stack;

    public MinStack() {
        stack = new Stack<Integer>(); //first element then min
    }
    
    private boolean isEmpty(){
        return stack.isEmpty();    
    }
    
    public void push(int x) {
        if (isEmpty()){
            stack.push(x);
            stack.push(x);
        } else {
            int min = stack.peek();
            stack.push(x);
            stack.push(Math.min(x, min));
        }        
    }
    
    public void pop() {
        stack.pop();
        stack.pop();
    }
    
    public int top() {
        int max = stack.pop();
        int val = stack.peek();
        stack.push(max);
        return val;
    }
    
    public int getMin() {
        return stack.peek(); 
    }
}