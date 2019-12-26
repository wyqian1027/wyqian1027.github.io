class Solution:
    
    def decodeString(self, s: str) -> str:
        
        stack = []
        stack.append(["", 1])
        n = 0
        
        for ch in s:
            
            if ch.isdigit():
                n = n * 10 + int(ch)
            elif ch == '[':
                stack.append(["", n])
                n = 0
            elif ch == ']':
                w, k = stack.pop();
                stack[-1][0] += w*k
            else:
                stack[-1][0] += ch
        
        return stack[0][0]