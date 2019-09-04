class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def helper(root): # max diff, min so far, max so far
            
            max_diff, min_sofar, max_sofar = 0, root.val, root.val

            if not root.left and not root.right:
                return max_diff, min_sofar, max_sofar

            if root.left:
                left = helper(root.left)
                max_diff = max(max_diff, left[0])
                min_sofar = min(min_sofar, left[1])
                max_sofar = max(max_sofar, left[2])
            if root.right:
                right = helper(root.right)
                max_diff = max(max_diff, right[0])
                min_sofar = min(min_sofar, right[1])
                max_sofar = max(max_sofar, right[2])

            max_diff = max(max_diff, root.val - min_sofar, max_sofar - root.val)

            return max_diff, min_sofar, max_sofar
            
        return helper(root)[0]