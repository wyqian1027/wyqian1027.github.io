# 1. Best solution: without using addition!
# Just use logic gates like XOR, AND, since A + B = (A XOR B) + (A & B) << 1. Basically,
# A XOR B : taking the sum without considering carry
# A & B   : tracking all the carries 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        x, y = int(a, 2), int(b, 2)
        while y > 0:
            s = x ^ y
            carry = (x & y) << 1
            x, y = s, carry
        return bin(x)[2:]

# 2. We can do it bit by bit as usual
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if a == "0": return b
        if b == "0": return a
        
        a = list(a)[::-1]
        b = list(b)[::-1]
        
        c = [0]* (max(len(a), len(b)) + 1)
        carry = 0
        
        for i in range(len(c)):
            d1 = int(a[i]) if i < len(a) else 0
            d2 = int(b[i]) if i < len(b) else 0
            s = carry + d1 + d2
            carry = s // 2
            s = s % 2
            c[i] = str(s)

        while c and c[-1] == "0": c.pop()
            
        return "".join(c[::-1])