# 1. DFS/Preorder

class Solution:
    def tree2str(self, root):
        
        self.res = ""
        
        def dfs(root):
            
            if not root: 
                self.res += "()"
                return

            self.res += "(" + str(root.val)
            
            if root.left or root.right:
                
                dfs(root.left)
                
            if root.right:
            
                dfs(root.right)
            
            self.res += ")"
            
        dfs(root)
        
        return self.res[1:-1]
        
# 2. Recursion

class Solution:
    def tree2str(self, root):
        
        if not root: return ''
        
        left = right = ''
        
        if (root.left or root.right):
            
            left = '(' + self.tree2str(root.left) + ')'
            
        if (root.right):
            
            right = '(' + self.tree2str(root.right) + ')'
            
        return str(root.val) + left + right