class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        self.res = []
        self.dfs(word, 0, [""])
        return self.res
    
    def dfs(self, word, idx, path):
        if idx >= len(word):
            self.res.append("".join(path))
            return
        
        self.dfs(word, idx+1, path+ [word[idx]])
            
        if not path[-1].isdigit():
            for k in range(idx, len(word)):
                w = k - idx + 1
                self.dfs(word, k+1, path+ [str(w)])