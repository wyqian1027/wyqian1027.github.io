# Both two pointer solutions: O(N) time

# 1. Sliding by counts
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = r = 0
        ans = 0
        count = {}
        
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            while len(count) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans

# 2. Sliding by right positions
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = r = 0
        ans = 0
        right_pos = {}
        
        while r < len(s):
            if len(right_pos) <= k:
                right_pos[s[r]] = r
                r += 1
            while len(right_pos) > k:
                if right_pos[s[l]] == l:
                    del right_pos[s[l]]
                l += 1
            ans = max(ans, r - l)
        return ans