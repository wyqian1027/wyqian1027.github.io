# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        if K == 0: return [target.val]
        
        p = {}
        q = collections.deque([(root, None)])        
        while q:
            node, parent = q.popleft()
            p[node] = parent
            if node == target: break
            if node.left: q.append((node.left, node))
            if node.right: q.append((node.right, node))
              
        self.ans = set()
        self.visited = set()
        start = target
        while start:
            self.addNodes(start, K)
            self.visited.add(start)
            start = p[start]
            K -= 1
        
        self.ans.discard(target.val)
        
        return list(self.ans)
                
    
    def addNodes(self, node, depth):
        
        if not node or node in self.visited: return
        
        if depth == 0:
            self.ans.add(node.val)
            return
        self.addNodes(node.left, depth-1)
        self.addNodes(node.right, depth-1)