class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        ans = 0, 0, 0  # maxLen, left, right
        
        for l in range(n):
            r = l
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans[0]:
                ans = r - l - 1, l + 1, r - 1
        
        for l in range(n-1):
            r = l+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans[0]:
                ans = r - l - 1, l + 1, r - 1   
        
        return s[ans[1]:ans[2]+1]