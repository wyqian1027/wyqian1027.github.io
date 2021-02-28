class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def dfs(path, leftP, rightP):
            if leftP == rightP == n:
                res.append(path)
                return
            if leftP > n or rightP > n or rightP > leftP:
                return
            dfs(path+"(", leftP+1, rightP)
            dfs(path+")", leftP, rightP+1)
        
        dfs("", 0, 0)
        return res