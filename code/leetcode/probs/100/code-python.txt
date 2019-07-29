#1. Using BFS queue
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        q = collections.deque([(p, q)])
        
        while q:
            n1, n2 = q.popleft()
            if not n1 and n2:
                return False
            if not n2 and n1:
                return False
            if n1 and n2:
                if n1.val != n2.val: return False
                q.append((n1.left, n2.left))
                q.append((n1.right, n2.right))
        return True
        
#2. Using Recursion
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q: return True
        if not p and q: return False
        if not q and p: return False
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True