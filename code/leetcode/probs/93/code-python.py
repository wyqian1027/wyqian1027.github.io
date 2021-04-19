class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []; n = len(s)
        
        def dfs(start, path):
            if len(path) == 4:
                if start == n: res.append(".".join(path))
                return
            if start >= n: return
            if (4-len(path))*3 < n-start: return
            
            if s[start] == "0":
                path.append("0")
                dfs(start+1, path)
                path.pop()
                return
            
            for i in range(start+1, min(n+1, start+4)):
                sub = s[start:i]
                if 0 <= int(sub) <= 255:
                    path.append(sub)
                    dfs(i, path)
                    path.pop()
                    
        dfs(0, [])
        return res
