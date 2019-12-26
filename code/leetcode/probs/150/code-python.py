class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
    
        stack = []
        OPERATIONS = set(["+", "-", "*", "/"])
        
        for token in tokens:
            
            if token in OPERATIONS:
                second = stack.pop();
                first = stack.pop();
                stack.append(self.calculate(first, second, token))
            else:
                stack.append(token)
        
        return int(stack[0]);
    
    def calculate(self, first, second, token):
        
        first, second = int(first), int(second)
        
        if token == "*": return first*second
        if token == "/": return first//second
        if token == "+": return first+second
        if token == "-": return first-second