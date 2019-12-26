class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.s = 0
        def dfs(root):                
            if root:
                dfs(root.right)
                root.val += self.s
                self.s = root.val
                dfs(root.left)
                
        dfs(root)
        
        return root