# 1. Recursion

class Solution:
    
    diff = float('inf')
    
    preVal = - float('inf')
    
    def minDiffInBST(self, root: TreeNode) -> int:
        
        if root:
            
            self.minDiffInBST(root.left)
            
            self.diff = min(self.diff, root.val - self.preVal)
            
            if self.diff == 1: return 1
            
            self.preVal = root.val
            
            self.minDiffInBST(root.right)
            
        return self.diff
        
# 2. Stack

class Solution:

    def minDiffInBST(self, root: TreeNode) -> int:
        
        diff = float('inf')
        stack = []
        cur = root
        
        preVal = -float('inf')
        
        while (cur or len(stack) > 0):
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
                        
            diff = min(diff, cur.val - preVal)
            preVal = cur.val
            if (diff == 1): return 1

            cur = cur.right

        return diff