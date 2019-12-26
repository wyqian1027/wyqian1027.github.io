# Using DP Cache

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        ct = collections.Counter() #map ID to occurence
        d = {}  #map node to ID
        self.ans = []
        
        def visit(root):
            if not root: return '#'
            if root in d:
                return d[root]
            else:
                nodeID = "{},{},{}".format(root.val, visit(root.left), visit(root.right))
                d[root] = nodeID
                ct[nodeID] += 1
                if ct[nodeID] == 2: 
                    self.ans.append(root)
                return d[root]
        
        visit(root)
        return self.ans
                
        