class Solution:

    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        q = collections.deque([root])
        
        while q and root:
            
            level = []
            first = None
            
            for _ in range(len(q)):
                node = q.popleft()
                if not first: first = node
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
        
            if not level: 
                return first.val
            
            q = collections.deque(level)
        
        return None