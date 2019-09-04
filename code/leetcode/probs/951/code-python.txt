# Canonical BFS
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        if not root1 and not root2: return True
        if (not root1 and root2) or (not root2 and root1): return False
        
        q = collections.deque([(root1, root2)])
        
        while q:
            n1, n2 = q.popleft()
            if n1.val != n2.val: return False
            pair1, pair2 = [], []
            if n1.left: pair1.append(n1.left)
            if n1.right: pair1.append(n1.right)
            if n2.left: pair2.append(n2.left)
            if n2.right: pair2.append(n2.right)
            if len(pair1) != len(pair2): return False
            pair1.sort(key=lambda x: x.val)
            pair2.sort(key=lambda x: x.val)
            while pair1:
                q.append((pair1.pop(), pair2.pop()))
        
        return True

# Recursion:
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        if not root1 and not root2:
            return True
        elif not root1 and root2:
            return False
        elif not root2 and root1:
            return False
        else:
            if root1.val != root2.val: return False
            if self.flipEquiv(root1.left, root2.left) and \
               self.flipEquiv(root1.right, root2.right):
                return True
            elif self.flipEquiv(root1.left, root2.right) and \
               self.flipEquiv(root1.right, root2.left):
                return True
            return False