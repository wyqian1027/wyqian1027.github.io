# O(LgN*LgN) (lgN=#digits)
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        
        num = list(map(int, str(N)))
        
        digit = []
        
        for i in range(len(num)):
            for x in range(1, 10):
                if digit + [x]*(len(num) - i) > num:
                    digit.append(x-1)
                    break
            if len(digit) != i + 1:
                digit.append(9)
        
        return int("".join(map(str, digit)))

# O(LgN)
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        
        num = list(map(int, str(N)))
        
        i = 0
        
        while i + 1 < len(num) and num[i] <= num[i+1]:
            i += 1
        # 33(3)222 
        while 0 <= i < len(num) - 1 and num[i] > num[i+1]:
            num[i] = num[i] - 1
            i -= 1
        # (2)22222
        i += 1
        num[i+1:] = [9]*(len(num)-(i+1))
        
        return int("".join(map(str, num)))