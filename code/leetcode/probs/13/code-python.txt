class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, \
             "C": 100, "D": 500, "M": 1000}
        
        cur_val = 0
        total = 0
        for ch in s[::-1]:
            if d[ch] >= cur_val:
                total += d[ch]
            else:
                total -= d[ch]
            cur_val = d[ch]
                
        return total