# Typical Sliding Window Problem, Use two pointers and Dict of last seen position.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}  # lastSeen, rightmost position
        maxL = 0
        l = 0
        for r, ch in enumerate(s):
            if ch not in d:
                d[ch] = r
            else:
                if l <= d[ch]:
                    maxL = max(maxL, r - l)
                    l = d[ch] + 1
                d[ch] = r
            maxL = max(maxL, r - l + 1)
        maxL = max(maxL, len(s) - l)
        return maxL