# Top Down Solution
class Solution:

    def rob(self, root: TreeNode) -> int:
        
        cache = {}
        
        def calculate(root):
            
            if not root: return 0
            
            if root in cache:
                return cache[root]
            
            res1 = calculate(root.left) + calculate(root.right)
            
            res2 = root.val
            
            if root.left:
                
                res2 += calculate(root.left.left) + calculate(root.left.right)
            
            if root.right:
                
                res2 += calculate(root.right.left) + calculate(root.right.right)
                
            cache[root] = max(res1, res2)
            
            return cache[root]
        
        return calculate(root)
            
            
            
        