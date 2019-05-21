# 1. DFS

class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        self.res = 0
        self.dfs(root, "")
        return self.res
        
    def dfs(self, root, path):
        
        if not root: return
        
        if not root.left and not root.right:
            self.res += int(path+str(root.val), 2)
            return
        
        if root.left:
            self.dfs(root.left, path+str(root.val))
            
        if root.right:
            self.dfs(root.right, path+str(root.val))
            
# 2. Recursion:

    def sumRootToLeaf(self, root, val=0):
    
        if not root: return 0
        
        val = val * 2 + root.val
        
        if root.left == root.right: return val
        
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)