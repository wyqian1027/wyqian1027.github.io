class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
    
        return res[::-1]