class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()
        def dfs(s, idx, part, path):
            if len(s) - idx < 4 - part:
                return           
            
            if part > 3:
                if idx >= len(s):
                    res.add(".".join(path)) 
                return
            
            if s[idx] == "0":
                dfs(s, idx+1, part+1, path+["0"])
            else:
                for k in range(idx, max(idx + 3, len(s))):
                    if 0 <= int(s[idx:k+1]) <= 255:
                        dfs(s, k+1, part+1, path+[s[idx:k+1]])
        dfs(s, 0, 0, [])
        return list(res)