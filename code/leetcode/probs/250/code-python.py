class Solution:

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        def dfs(root):
            
            if not root: return True
                        
            L, R = dfs(root.left), dfs(root.right)
            
            if root.left and root.left.val != root.val:
                L = False
            if root.right and root.right.val != root.val:
                R = False
                
            if L and R: 
                self.count += 1
                return True
            
            return False
        
        self.count = 0
        
        dfs(root)
        
        return self.count
                
                
            
            