class Solution:
    
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        level = [root]
        ans = []
        
        while root and level:
            
            ans.append( [x.val for x in level] )
            
            children = [x.children for x in level]
            
            level = [x for el in children for x in el if x != None]
            
        return ans