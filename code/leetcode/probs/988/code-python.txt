# Solve the DFS reversely!

class Solution:

    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        d = {i: x for i, x in enumerate('abcdefghijklmnopqrstuvwxyz')}
        self.res = "z"*8500
        
        def dfs(root, path):
            
            if not root: return
            
            cur = d[root.val]
            
            if not root.left and not root.right:
                self.res = min(self.res, cur+path)
            
            dfs(root.left, cur+path)
            dfs(root.right, cur+path)
        
        dfs(root, "")

        return self.res
    

                    
                    
                
                
                