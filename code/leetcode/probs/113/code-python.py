class Solution:
    def pathSum(self, root, target):
        
        res = []
        
        def dfs(root, curSum, path, res):
            
            if not root:
                return
            
            if not root.left and not root.right and curSum + root.val == target:
                res.append(path+[root.val])
                return
            
            if root.left:
                dfs(root.left, curSum+root.val, path+[root.val], res)
                
            if root.right:
                dfs(root.right, curSum+root.val, path+[root.val], res)
            
        dfs(root, 0, [], res)
        
        return res
                
        