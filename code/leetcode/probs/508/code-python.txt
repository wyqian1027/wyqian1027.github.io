class Solution:

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        self.d = {}
        self.maxCount = 0
        self.ans = []
        
        self.traverse(root)
        
        return self.ans

    def traverse(self, root):
        
        if not root: return 0    
        
        s = root.val + self.traverse(root.left) + self.traverse(root.right)

        self.d[s] = self.d.get(s, 0) + 1
        
        if self.d[s] > self.maxCount:
            self.maxCount += 1
            self.ans = [s]
            
        elif self.d[s] == self.maxCount:
            self.ans.append(s)            

        return s