class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        
        res = []
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        if sum(d[ch] % 2 == 1 for ch in d) > 1:
            return res
        
        mid = ""
        for ch in d:
            if d[ch] % 2 == 1: 
                mid = ch
                break        
    
        def dfs(path, res):
            if len(path) == len(s) // 2:
                res.append(path[:]+mid+path[::-1])
                return
            for ch in d:
                if d[ch] >= 2:
                    d[ch] -= 2
                    dfs(path+ch, res)
                    d[ch] += 2
        dfs("", res)
        return res