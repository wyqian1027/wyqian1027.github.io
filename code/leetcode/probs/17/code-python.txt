class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d = {"2": ["a", "b", "c"],
             "3": ["d", "e", "f"],
             "4": ["g", "h", "i"],
             "5": ["j", "k", "l"],
             "6": ["m", "n", "o"],
             "7": ["p", "q", "r", "s"],
             "8": ["t", "u", "v"],
             "9": ["w", "x", "y", "z"]}
        
        res = []
        
        if not digits: return []
        
        def dfs(digits, path, res):
            
            if not digits:
                res.append(path)
                return
            
            for ch in d[digits[0]]:
                dfs(digits[1:], path+ch, res)
            
        dfs(digits, "", res)
        
        return res