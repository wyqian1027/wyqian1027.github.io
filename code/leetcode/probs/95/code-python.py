# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        if n <= 0: return []
        
        self.cache = {}  # tuple of (left, right) -> list of Tree roots
        
        def buildBST(left, right):
            
            if left > right:
                return [None]
            
            if (left, right) in self.cache:
                return self.cache[(left, right)]
            
            res = []            
            
            for rootVal in range(left, right + 1):
                for leftNode in buildBST(left, rootVal-1):
                    for rightNode in buildBST(rootVal+1, right):
                        root = TreeNode(rootVal)
                        root.left = leftNode
                        root.right = rightNode
                        res.append(root)
            
            self.cache[(left, right)] = res
            
            return res
        
        return buildBST(1, n)