class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def findDepth(root):
            if not root:
                return 0, True
            left, b1 = findDepth(root.left)
            right, b2 = findDepth(root.right)
            ans = 1 + max(left, right)
            if abs(left - right) <= 1 and b1 and b2:
                return ans, True
            else:
                return ans, False
        
        return findDepth(root)[1]

# Even more optimized
# Use -1 as flag
# Ignore checking right if unsatisfied

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def findDepth(root):
            if not root:
                return 0
            left = findDepth(root.left)
            if left == -1:
                return -1
            right = findDepth(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        
        return findDepth(root) != -1