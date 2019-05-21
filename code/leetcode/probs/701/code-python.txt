class Solution:

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        node = root
        
        while node:
            
            if val > node.val:
                
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                
                node = node.right
                
            else:
                
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                
                node = node.left
                
        return TreeNode(val)