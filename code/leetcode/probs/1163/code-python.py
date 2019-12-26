# THis is O(N^2) worst case
class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        start_loc = n
        for i in range(n-1, -1, -1):
            if start_loc != n and s[start_loc] == s[i] and i + 1 == start_loc:
                start_loc = i
                continue
            ch = s[i]
            if start_loc == n or ch > s[start_loc]:
                start_loc = i
            elif ch == s[start_loc]:
                better = True
                for j in range(n - start_loc):
                    if s[i+j] > s[start_loc + j]:
                        break
                    elif s[i+j] < s[start_loc + j]:
                        better = False
                        break
                if better :
                    start_loc = i
        return s[start_loc:]