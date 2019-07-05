# 1. Using chr and ord
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        total = 0
        for i in range(len(s)):
            total += ord(t[i]) - ord(s[i])
        total += ord(t[-1])
        return chr(total)

# 2. Using XOR
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ord(t[-1])
        for i in range(len(s)):
            res ^= ord(s[i])
            res ^= ord(t[i])
        return chr(res)

# 3. Using collections.Counter