# 1 DFS without cache

class Solution:

    def pathSum(self, root: TreeNode, target: int) -> int:
        
        self.count = 0
        
        def dfs(node):
            
            if not node: return []
                
            if not node.left and not node.right:

                if node.val == target: self.count += 1

                return [node.val]

            left = dfs(node.left)
            right = dfs(node.right)
            
            res = [x + node.val for x in left] + \
                  [x + node.val for x in right] + \
                  [node.val]
            
            for x in res:
                if x == target: self.count += 1
            
            return res

        dfs(root)
        
        return self.count

# 2 DFS with cache, backtracking

class Solution:

    def pathSum(self, root: TreeNode, s: int) -> int:

        self.result = 0
        cache = {0:1}
        
        self.dfs(root, s, 0, cache)
        
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):

        if root is None:
            return  
        
        currPathSum += root.val
        oldPathSum = currPathSum - target

        self.result += cache.get(oldPathSum, 0)
        
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        

        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)

        cache[currPathSum] -= 1