class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ct = collections.Counter(s)
        oddCount = 0
        for k in ct:
            if ct[k] % 2 == 1: oddCount += 1
        return oddCount <= 1