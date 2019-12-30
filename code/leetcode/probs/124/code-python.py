class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.maxSum = float('-inf')
        
        def maxGain(root):   
            '''
            Compute maxPathSum centered at this root.
            1. leftGain and rightGain have ceiling 0
            2. maxPathSum = root.val + leftGain + rightGain
            3. passing only the bigger gain (left or right) to recursion stack
            '''

            if not root: return 0
            
            leftGain = max(maxGain(root.left), 0)
            rightGain = max(maxGain(root.right), 0)
            
            self.maxSum = max(self.maxSum, root.val + leftGain + rightGain)
            
            return root.val + max(leftGain, rightGain)
    
        maxGain(root)
        return self.maxSum

# same idea but without global variable:
# helper function returns a tuple:
# (max path sum at this node, at its left branch, at its right branch)
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def helper(root):   
            
            if not root: return float('-inf'), 0, 0
            
            max_left, l1, l2 = helper(root.left)
            max_right, r1, r2 = helper(root.right)
            
            max_node = max(l1, l2, 0) + max(r1, r2, 0) + root.val
            
            return max(max_node, max_left, max_right), \
                max(l1, l2, 0) + root.val, \
                max(r1, r2, 0) + root.val
    
        return helper(root)[0]