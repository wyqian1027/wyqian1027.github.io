class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        def helper(root):
            if not root:
                return 0, 0, float('inf'), float('-inf')
            n1, c1, min1, max1 = helper(root.left)
            n2, c2, min2, max2 = helper(root.right)
            n = c1 + c2 + 1 if max1 < root.val < min2 else float('-inf')
            return max(n, n1, n2), n, min(root.val, min1), max(root.val, max2)
        
        return helper(root)[0]