class Solution:
    
    def largestValues(self, root: TreeNode) -> List[int]:
        
        q = collections.deque([root])
        
        ans = []
        
        while root and q:
            
            curMax = -float('inf')
            
            for _ in range(len(q)):
                
                node = q.popleft()
                
                curMax = max(curMax, node.val)
                
                if node.left: q.append(node.left)
                    
                if node.right: q.append(node.right)
                
            ans.append(curMax)
            
        return ans
        