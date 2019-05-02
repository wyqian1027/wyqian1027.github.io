class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

#1. Recursion
class Solution:
    def maxDepth(self, root):
        
        if not root:
            return 0
        
        h = 0
        for ch in root.children:
            h = max(h, self.maxDepth(ch))
        
        return h + 1
   
#2. DFS (Stack) 
class Solution:
    
    def maxDepth(self, root):
        
        if not root: return 0
        
        stack = [(1, root)]
        
        h = 0
        
        while stack:
            
            curDepth, curNode = stack.pop()
            
            h = max(h, curDepth)
            
            for child in curNode.children:
                
                stack.append((curDepth + 1, child))
            
        return h

#3. DFS (Backtracking) 
class Solution:        
    def maxDepth(self, root):
        
        self.h = 0
        
        def dfs(node, depth):
            
            if not node:
                self.h = max(self.h, depth)
                return
            
            if not node.children:
                self.h = max(self.h, depth + 1)
                return
            
            else:
                for ch in node.children:
                    dfs(ch, depth + 1)
                
        dfs(root, 0)
        
        return self.h