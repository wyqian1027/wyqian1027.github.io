"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        res = []
        stack = [root]
        
        if not root: return []
        
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])
        
        return res