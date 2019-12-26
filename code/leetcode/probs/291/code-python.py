# Backtracking DFS solution

class Solution:
    
    def wordPatternMatch(self, p: str, s: str) -> bool:

        def dfs(p, s, d):

            if p == "" and s == "": return True
            if p == "" and s != "": return False          
            
            for end in range(1, len(s) - len(p) + 2):
                
                if p[0] not in d and s[:end] not in d.values():
                    d[p[0]] = s[:end]
                    if dfs(p[1:], s[end:], d): return True
                    del d[p[0]]
                elif p[0] in d and d[p[0]] == s[:end]:
                    if dfs(p[1:], s[end:], d): return True
            
            return False
        
        return dfs(p, s, {})