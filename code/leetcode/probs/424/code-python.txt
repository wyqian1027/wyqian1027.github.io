class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        res = 0
        
        # count for the sliding window
        d = collections.Counter()
        max_freq = 0
        
        while right < len(s):
            d[s[right]] += 1
            # max_freq = d.most_common(1)[0][1]
            max_freq = max(max_freq, d[s[right]])
            if right - left + 1 - max_freq > k:
                d[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res