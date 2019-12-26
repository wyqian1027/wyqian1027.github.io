# 1. Without Dict
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root is p or root is q:
            return root
            
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right: 
            return root
        else:
            return left or right

# 2. With Parent Dict
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        d = {}
        def buildParent(root, parent):
            if root:
                d[root] = parent
                buildParent(root.left, root)
                buildParent(root.right, root)
        buildParent(root, None)
        st = set()
        while p:
            st.add(p)
            p = d[p]
        while q not in st:
            q = d[q]
        return q