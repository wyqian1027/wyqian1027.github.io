# 1. Recursion with Return Node
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        res = []
        to_delete = set(to_delete)
        
        def visit(root, is_root):
            if not root: return None
            is_delete = root.val in to_delete 
            if not is_delete and is_root: 
                res.append(root)
            root.left = visit(root.left, is_delete)
            root.right = visit(root.right, is_delete)
            return None if is_delete else root
        
        visit(root, True)
        return res

# 2. Recursion without

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        res = []
        to_delete = set(to_delete)
        
        def visit(node, is_root):
            
            if not node: return
            
            is_delete = node.val in to_delete 
            
            if not is_delete and is_root: 
                res.append(node)
            
            visit(node.left, is_delete)
            visit(node.right, is_delete)
            
            if node.left and node.left.val in to_delete:
                node.left = None
            if node.right and node.right.val in to_delete:
                node.right = None
            
        visit(root, root not in to_delete)

        return res