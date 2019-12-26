class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        d1 = {}
        for ch in s1:
            d1[ch] = d1.get(ch, 0) + 1
        
        window = {}
        j = 0
        
        for i, ch in enumerate(s2):
            if ch not in d1:
                window = {}
                j = i + 1
            else:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] > d1[ch]:
                    while j < i and s2[j] != ch:
                        window[s2[j]] -= 1
                        j += 1
                    window[ch] -= 1
                    j += 1
                        
                elif window[ch] == d1[ch]:
                    if all(window.get(ch, 0) == d1[ch] for ch in d1):
                        return True
        
        return False