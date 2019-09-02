class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        
        if not root: return [None, None]
        
        if root.val <= V:
            left_sub, right_sub = self.splitBST(root.right, V)
            root.right = left_sub
            return [root, right_sub]
        else:
            left_sub, right_sub = self.splitBST(root.left, V)
            root.left = right_sub
            return [left_sub, root]