# 1. Recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# 2. Using stack and pointer
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        res = []
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
    
        return res