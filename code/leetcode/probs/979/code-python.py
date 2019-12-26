class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        
        self.count = 0
        
        def dfs(node):
            if not node:
                return 0
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                self.count += abs(left) + abs(right)
                return left + right + node.val - 1
                # positive, send to parent
                # nega, request from parent
                
        dfs(root)
        return self.count