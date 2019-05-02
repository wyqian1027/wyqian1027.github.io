class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        
        level = [root]
        res = []
        
        while level:
            res.append([node.val for node in level])
            nxtLevel = [(node.left, node.right) for node in level]
            level = [node for pair in nxtLevel for node in pair if node]
        return res
                    
            
            
            