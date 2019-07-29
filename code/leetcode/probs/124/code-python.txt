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