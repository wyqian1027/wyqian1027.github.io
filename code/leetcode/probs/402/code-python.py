class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k > len(num): return "0"
        stack = ["0"]
        
        for ch in num:
            while stack and stack[-1] > ch and k > 0:
                stack.pop()
                k -= 1
            stack.append(ch)
                    
        while k > 0:
            stack.pop()
            k -= 1
            
        return str(int("".join(stack)))