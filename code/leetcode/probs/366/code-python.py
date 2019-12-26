class Solution:

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        
        ans = []
        self.cache = {}
        self.find(root)

        for i in range(1, max(self.cache.values())+1):
            ans.append([x.val for x in self.cache if self.cache[x] == i])
            
        return ans
    
    def find(self, root):
        
        if not root: return 0
        if root in self.cache: 
            layer = self.cache[root]
        else:
            layer = 1 + max(self.find(root.left), self.find(root.right))
            self.cache[root] = layer
        
        return layer        
        