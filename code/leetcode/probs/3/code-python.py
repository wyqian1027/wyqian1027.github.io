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

# Improved versions:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = collections.Counter()  # naive first solution using counts (Big O is not optimal, O(26N))
        ans = i = 0
        for j in range(len(s)):
            ch = s[j]
            count[ch] += 1
            while any(count[c] > 1 for c in count):
                count[s[i]] -= 1
                i += 1
            ans = max(ans, j-i+1)
        return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        loc = {} # map of locations within the window, O(2N)
        ans = i = j = 0
        while j < len(s):
            if s[j] not in loc:
                loc[s[j]] = j
                ans = max(ans, j - i + 1)
                j += 1
            else:
                del loc[s[i]]
                i += 1
        return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:            
        loc = {}  # map of locations last seen (could be outside window), O(N)
        ans = i = j = 0
        while j < len(s):
            # max is to ensure windows moves rightward
            if s[j] in loc:
                i = max(i, loc[s[j]] + 1)
            # update last seen location
            loc[s[j]] = j
            ans = max(ans, j - i + 1)
            j += 1
        return ans



        
