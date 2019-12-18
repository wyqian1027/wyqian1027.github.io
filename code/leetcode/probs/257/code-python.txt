class Solution:
    def binaryTreePaths(self, root):
        
        def dfs(root, path, res):
            if not root.left and not root.right:
                res.append(path)
                return
            if root.left:
                dfs(root.left, path + "->" + str(root.left.val), res)
            if root.right:
                dfs(root.right, path + "->" + str(root.right.val), res)
                
        if not root: return []
        res = []
        dfs(root, str(root.val), res)
        
        return res

# Cleaner:
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        self.res = []
        self.dfs(root, "")
        return self.res
        
    def dfs(self, root, path):

        if not root: return
        
        path = path + str(root.val)
        if not root.left and not root.right:
            self.res.append(path)
        else:
            path = path + "->"
            self.dfs(root.left, path)
            self.dfs(root.right, path)