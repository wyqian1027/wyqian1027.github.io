class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        
        if n == 0: return "0"
        
        is_neg = (n < 0 and d > 0) or (n > 0 and d < 0)
        
        n, d = abs(n), abs(d)
        
        integ, frac = divmod(n, d)
        
        if frac == 0: return "-" + str(integ) if is_neg else str(integ)
        
        decimals = []
        repeat = None
        seen = {}    # store n, d pairs, if seen then must be repeating
        index = 1
        
        while frac != 0:
            
            if frac in seen:
                repeat = index - seen[frac]
                break
                
            seen[frac] = index
            digit, frac = divmod(10*frac, d)
            decimals.append(digit)
            index += 1

        out = str(integ) + "." + "".join(map(str, decimals))
        
        if repeat: out = out[:-repeat] + "(" + out[-repeat:] + ")"
        if is_neg: out = "-" + out
            
        return out