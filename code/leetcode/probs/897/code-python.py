class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(root):
            if root:
                inorder(root.left)
                root.left = None
                self.cur.right = root
                self.cur = root
                inorder(root.right)
        
        dummy = self.cur = TreeNode(0)
        inorder(root)
        
        return dummy.right