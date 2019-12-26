class Solution:

    def calculate(self, s: str) -> int:
        
        res = 0
        number = 0
        sign = 1
        stack = []
        
        for ch in s:
            
            if "0" <= ch <= "9":
                number = number*10 + int(ch)
                
            elif ch == "+":
                res += number*sign
                number = 0
                sign = 1
            
            elif ch == "-":
                res += number*sign
                number = 0
                sign = -1
            
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            
            elif ch == ")":
                res += number*sign
                res *= stack.pop()
                res += stack.pop()
                number = 0
                sign = 1
        
        if number != 0:
            return res += number*sign
        
        return res