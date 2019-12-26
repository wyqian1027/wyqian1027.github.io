class Solution:
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        q = collections.deque([(None, root)])
        
        d = {}
        
        while q:
                       
            for _ in range(len(q)):
            
                parent, node = q.popleft()

                if node.val == x or node.val == y:
                    d[node.val] = parent
                
                if node.left: 
                    q.append((node, node.left))

                if node.right: 
                    q.append((node, node.right))
                        
            
            if len(d) == 1: return False
            
            if len(d) == 2 and len(set(d.values())) == 2: return True
            
        return False