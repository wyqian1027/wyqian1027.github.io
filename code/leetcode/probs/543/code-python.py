# Diameter of Tree is defined 
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
               
        def helper(root):
            # diameter at this level, longest path going down at this level
            if not root: return 0, 0   
            maxL, pathL = helper(root.left)
            maxR, pathR = helper(root.right)
            path = max(pathL, pathR) + 1
            diameter = max(maxL, maxR, pathL + pathR + 1)
            return diameter, path
        
        return max(0, helper(root)[0] - 1)