# Improved Version, though both O(S+T)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = r = 0
        tDict = collections.Counter(t)
        required = len(tDict)
        formed = 0
        window = {}
        ans = float('inf'), 0, 0
        
        while r < len(s):
            ch = s[r]
            if ch not in tDict: 
                r += 1
                continue
                
            window[ch] = window.get(ch, 0) + 1
            if tDict[ch] == window[ch]:
                formed += 1
                
            # if a window is found (formed == required), contract it to get the smallest possible
            while formed == required and l <= r:
                leftCh = s[l]
                if leftCh in tDict:
                    if r - l + 1  < ans[0]:
                        ans = r - l + 1, l, r
                    window[leftCh] -= 1
                    if window[leftCh] < tDict[leftCh]:
                        formed -= 1
                l += 1
            r += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]

# Vanilla Version
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = r = 0
        tDict = collections.Counter(t)
        required = len(tDict)
        formed = 0
        window = {}
        ans = float('inf'), 0, 0
        
        while r < len(s):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1
            if ch in tDict and tDict[ch] == window[ch]:
                formed += 1
            # print(r, formed, required, window)
            while formed == required and l <= r:
                leftCh = s[l]
                if r - l + 1  < ans[0]:
                    ans = r - l + 1, l, r
                l += 1
                window[leftCh] -= 1
                if leftCh in tDict and window[leftCh] < tDict[leftCh]:
                    formed -= 1
            r += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]