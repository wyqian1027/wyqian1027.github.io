# 1. DFS
class Solution:
    def hasPathSum(self, root, target):
        
        def dfs(root, curSum):
            
            if not root: 
                return False
            
            if not root.left and not root.right:
                return root.val + curSum == target
                        
            return dfs(root.left, curSum + root.val) or \
                dfs(root.right, curSum + root.val)
    
        return dfs(root, 0)

# 2. Stack, Iteration
class Solution:
    def hasPathSum(self, root, target):
        
        if not root:
            return False
        
        stack = [(root, root.val)]
        
        while stack:
            node, s = stack.pop()
            if not node.left and not node.right and s == target:
                return True
            if node.left:
                stack.append((node.left, s + node.left.val))
            if node.right:
                stack.append((node.right, s + node.right.val))
        
        return False