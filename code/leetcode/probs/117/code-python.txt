class Solution:
    def connect(self, root: 'Node') -> 'Node':

        head = root
        
        q = collections.deque([root])
        
        while q and root:
            
            level = []
            for i in range(len(q)):
                node = q.popleft()
                node.next = None
                level.append(node)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            for i in range(len(level)-1):
                level[i].next = level[i+1]
        
        return head