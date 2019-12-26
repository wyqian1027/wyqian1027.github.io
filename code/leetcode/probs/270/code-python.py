class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        ans = root.val
        
        while root:
            
            if abs(root.val - target) < abs(target - ans):
                ans = root.val
            
            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            else:
                return root.val
        
        return ans
        