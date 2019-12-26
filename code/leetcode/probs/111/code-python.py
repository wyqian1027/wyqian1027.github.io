#1. Recursion
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
           
        if not root.left and not root.right:
            return 1

        h = float('inf')
        if root.left:
            h = min(h, self.minDepth(root.left))
        if root.right:
            h = min(h, self.minDepth(root.right))
            
        return 1 + h

#2. Level traversal (BFS)
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root: return 0
        
        level = [root]
        ans = 1
        
        while level:
            nextLevel = []
            for node in level:
                L = node.left
                R = node.right
                if not L and not R: return ans
                if L: nextLevel.append(L)
                if R: nextLevel.append(R)
            level = nextLevel
            ans += 1