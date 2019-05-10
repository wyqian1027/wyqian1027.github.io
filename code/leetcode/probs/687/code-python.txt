# res stores the number of nodes on the unival path, to get edges - 1

class Solution:

    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        if not root: return 0
        
        self.res = 1
        
        def dfs(root):
            
            if not root: return (0, 0) # can be ignored since root always valid
            
            if not root.left and not root.right:
                return (1, 1)
            
            L, R = 1, 1
            
            left, right = dfs(root.left), dfs(root.right)
            
            if root.left and root.left.val == root.val:
                
                L = max(left) + 1
            
            if root.right and root.right.val == root.val:
                
                R = max(right) + 1
            
            self.res = max(self.res, L + R - 1)
            
            return (L, R)
    
        dfs(root)
        
        return self.res - 1
            
                
            