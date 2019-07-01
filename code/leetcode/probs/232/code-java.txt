class MyQueue {

    Stack<Integer> pushStack;
    Stack<Integer> popStack;
    
    public MyQueue() {
        pushStack = new Stack<Integer>();    
        popStack = new Stack<Integer>();    
    }
    
    public void push(int x) {
        pushStack.push(x);
    }
    
    public int pop() {
        if (popStack.isEmpty()){
            while (!pushStack.isEmpty())
                popStack.push(pushStack.pop());
        }        
        return popStack.pop();
    }
    
    public int peek() {
        int element = pop();
        popStack.push(element);
        return element;
    }
    
    public boolean empty() {
        return popStack.isEmpty() && pushStack.isEmpty();
    }
}

// or...
class MyQueue {

    Stack<Integer> input = new Stack();
    Stack<Integer> output = new Stack();
    
    public void push(int x) {
        input.push(x);
    }

    public int pop() {
        peek();
        return output.pop();
    }

    public int peek() {
        if (output.isEmpty())
            while (!input.isEmpty())
                output.push(input.pop());
        return output.peek();
    }

    public boolean empty() {
        return input.empty() && output.empty();
    }

}