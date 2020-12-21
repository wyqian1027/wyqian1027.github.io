class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        def helper(root):
            # returns (tilt, sum of subtree, sum of total tilts so far) of this node
            if not root: return 0, 0, 0
            L_t, L_s, L_tot = helper(root.left)
            R_t, R_s, R_tot = helper(root.right)
            tilt = abs(L_s - R_s)
            s = L_s + R_s + root.val
            total = L_tot + R_tot + tilt
            return tilt, s, total
        
        return helper(root)[2]