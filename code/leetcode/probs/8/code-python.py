class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()
        num = 0
        sign = None
        INT_MAX = 2**31-1; INT_MIN = -2**31
        
        for a in s:
            # a = digit or non-digit (check sign first time only)
            if a in ["+", "-"] and sign == None:
                sign = 1 if a == "+" else -1
                
            elif not a.isdigit():
                return num
            
            else:
                if sign == None: sign = 1
                num = num*10
                num = num + int(a) if sign == 1 else num - int(a)
                if sign == 1 and num >= INT_MAX:
                    return INT_MAX
                if sign == -1 and num <= INT_MIN:
                    return INT_MIN
        return num
