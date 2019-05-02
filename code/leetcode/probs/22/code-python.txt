class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(left, right, path, res):
            
            if left < right or left > n or right > n:
                return
            
            if left == n and right == n:
                res.append(path)
                
            dfs(left+1, right, path[:]+"(", res)
            dfs(left, right+1, path[:]+")", res)      
        
        res = []
        dfs(0, 0, "", res)
        
        return res