class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def dfs(root):
            
            if not root: return
            
            if L <= root.val <= R:
                self.res += root.val
                dfs(root.left)
                dfs(root.right)
            elif root.val < L:
                dfs(root.right)
            else:
                dfs(root.left)
                
        self.res = 0
        dfs(root)
        
        return self.res