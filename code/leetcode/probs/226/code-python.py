#1. Recursion
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root: return
        
        L = self.invertTree(root.right)
        R = self.invertTree(root.left)
        root.left = L
        root.right = R
        
        return root

#2. Level by Level Iteration
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root: return
        
        q = collections.deque([root])
        
        while q:
            
            node = q.popleft()
            
            node.left, node.right = node.right, node.left
            
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        return root   