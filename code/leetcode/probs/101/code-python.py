#1. Recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root: return True
        
        def check(n1, n2):
            
            if not n1 and not n2:
                return True
            elif n1 and n2 and n1.val == n2.val and \
            check(n1.left, n2.right) and check(n1.right, n2.left):
                return True
            else:
                return False
            
        return check(root.left, root.right)  
  
#2. Iteration, Level by Level   
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root: return True
        
        q = collections.deque([])
        q.append(root)
        q.append(root)
        
        while q:
            n1 = q.pop()
            n2 = q.pop()
            if not n1 and not n2:
                continue
            elif (n1 and not n2) or (n2 and not n1):
                return False
            else:
                if n1.val != n2.val: return False
                q.append(n1.left)
                q.append(n2.right)
                q.append(n1.right)
                q.append(n2.left)   
        
        return True