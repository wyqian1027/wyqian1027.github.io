class Solution:

    def isUnivalTree(self, root: TreeNode) -> bool:
        
        if not root: return True
        
        L, R = True, True
        
        if root.left:
            
            L = root.val == root.left.val and self.isUnivalTree(root.left)
            
        if root.right:
            
            R = root.val == root.right.val and self.isUnivalTree(root.right)
            
        return L and R    