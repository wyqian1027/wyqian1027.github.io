# 1. DFS

class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        
        self.paths = []
        
        def dfs(root, curPath):
            
            if not root: return
            
            if not root.left and not root.right:
                self.paths.append(curPath + str(root.val))
                
            if root.left:
                dfs(root.left, curPath + str(root.val))
                
            if root.right:
                dfs(root.right, curPath + str(root.val))
        
        dfs(root, "")
        
        return sum(map(int, self.paths))

# 2. More natural forward DFS:

class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        
        self.res = 0
        
        def dfs(root, curSum):
            
            if root:
                
                if not root.left and not root.right:
                    self.res += 10*curSum + root.val
                
                if root.left:
                    dfs(root.left, 10*curSum + root.val)
                    
                if root.right:
                    dfs(root.right, 10*curSum + root.val)
        
        dfs(root, 0)
        
        return self.res
                
            
        
        
        