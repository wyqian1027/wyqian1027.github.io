class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        n, s = x, 0
        while n != 0:
            s = 10*s + (n % 10)
            n //= 10
        return s == x    