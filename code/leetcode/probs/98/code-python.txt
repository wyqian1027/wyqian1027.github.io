class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(root, lo, hi):
            if not root:
                return True
            if lo < root.val < hi and \
            helper(root.left, lo, root.val) and \
            helper(root.right, root.val, hi):
                return True
            return False
        
        return helper(root, -float('inf'),  float('inf'))